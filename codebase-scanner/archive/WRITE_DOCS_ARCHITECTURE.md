# --write-docs Feature Architecture

## System Overview

```mermaid
graph TB
    User[User runs scanner.py --write-docs]
    Scanner[scanner.py CLI]
    InitScan[Initial Scan]
    CheckEnv[Check Environment Variables]
    LoadResults[Load Scan Results]
    DocGen[DocumentationGenerator]
    WatsonX[WatsonxClient]
    PythonWriter[PythonDocumentationWriter]
    DocInserter[DocumentationInserter]
    Backup[Create Backup]
    Insert[Insert Docstrings]
    Validate[Validate Syntax]
    Rescan[Re-scan Codebase]
    Report[Generate Report]
    
    User --> Scanner
    Scanner --> InitScan
    InitScan --> CheckEnv
    CheckEnv -->|Missing| Error[Exit with Error Message]
    CheckEnv -->|Valid| LoadResults
    LoadResults --> DocGen
    DocGen --> PythonWriter
    PythonWriter --> WatsonX
    WatsonX -->|Generate Docstring| PythonWriter
    PythonWriter --> DocInserter
    DocInserter --> Backup
    Backup --> Insert
    Insert --> Validate
    Validate -->|Invalid| Rollback[Restore from Backup]
    Validate -->|Valid| Rescan
    Rescan --> Report
    Report --> User
```

## Component Interaction Flow

```mermaid
sequenceDiagram
    participant User
    participant Scanner
    participant DocGen as DocumentationGenerator
    participant Writer as PythonDocumentationWriter
    participant WatsonX as WatsonxClient
    participant Inserter as DocumentationInserter
    participant FileSystem
    
    User->>Scanner: python scanner.py --write-docs
    Scanner->>Scanner: Run initial scan
    Scanner->>Scanner: Check environment variables
    Scanner->>DocGen: generate_documentation(scan_results)
    
    loop For each undocumented file
        DocGen->>Writer: generate_function_doc(func_info)
        Writer->>Writer: Extract function signature & body
        Writer->>WatsonX: generate_docstring(signature, body)
        WatsonX->>WatsonX: Call granite-3-8b-instruct API
        WatsonX-->>Writer: Return generated docstring
        Writer->>Writer: Validate & format docstring
        Writer-->>DocGen: Return formatted docstring
        
        DocGen->>Inserter: insert_documentation(file_path, doc_items)
        Inserter->>FileSystem: Create .bak backup
        Inserter->>Inserter: Insert docstrings with proper indentation
        Inserter->>FileSystem: Write to temp file
        Inserter->>Inserter: Validate Python syntax
        
        alt Syntax Valid
            Inserter->>FileSystem: Atomic replace original file
            Inserter-->>DocGen: Success
        else Syntax Invalid
            Inserter->>FileSystem: Restore from backup
            Inserter-->>DocGen: Error
        end
    end
    
    DocGen-->>Scanner: Return GenerationReport
    Scanner->>Scanner: Re-scan codebase
    Scanner->>User: Display before/after comparison
```

## Data Flow

```mermaid
graph LR
    A[Scan Results JSON] --> B[Filter Python Files]
    B --> C[Filter Undocumented Items]
    C --> D[Extract Function Context]
    D --> E[Generate Prompt]
    E --> F[watsonx.ai API]
    F --> G[Parse Response]
    G --> H[Format Docstring]
    H --> I[Insert into File]
    I --> J[Validate Syntax]
    J --> K[Updated Source File]
    K --> L[Re-scan]
    L --> M[Coverage Report]
```

## Module Structure

```
codebase-scanner/
│
├── scanner.py                    # Main CLI entry point
│   ├── main()                    # Parse args, orchestrate workflow
│   ├── scan_codebase()          # Existing scan functionality
│   └── [NEW] --write-docs flag  # Trigger documentation generation
│
├── core/
│   ├── walker.py                # Directory traversal (existing)
│   ├── extractor.py             # Metadata extraction (existing)
│   └── doc_generator.py         # [NEW] Documentation orchestrator
│       ├── generate_documentation()
│       ├── _process_file()
│       ├── _filter_python_files()
│       └── _filter_undocumented()
│
├── writers/                      # [NEW] Documentation generation
│   ├── __init__.py
│   ├── base_writer.py           # Abstract base class
│   │   ├── generate_function_doc()
│   │   ├── generate_class_doc()
│   │   ├── generate_method_doc()
│   │   └── validate_documentation()
│   │
│   ├── watsonx_client.py        # watsonx.ai API client
│   │   ├── __init__()           # Load credentials from env
│   │   ├── generate_docstring() # Call granite-3-8b-instruct
│   │   ├── _build_prompt()      # Construct API prompt
│   │   └── _handle_response()   # Parse API response
│   │
│   ├── python_writer.py         # Python-specific writer
│   │   ├── generate_function_doc()
│   │   ├── generate_class_doc()
│   │   ├── generate_method_doc()
│   │   ├── _extract_signature()
│   │   ├── _extract_body()
│   │   └── _format_docstring()
│   │
│   └── doc_inserter.py          # Safe file modification
│       ├── insert_documentation()
│       ├── create_backup()
│       ├── validate_python_syntax()
│       ├── restore_backup()
│       └── _get_indentation()
│
├── parsers/                      # Existing parsers
│   └── python_parser.py         # Extract function/class metadata
│
└── formatters/                   # Existing formatters
    ├── json_formatter.py        # JSON output
    └── markdown_formatter.py    # Markdown output
```

## Key Design Patterns

### 1. Strategy Pattern
- **BaseDocumentationWriter** defines interface
- Language-specific writers implement strategy
- Easy to add new languages (JavaScript, Java, C++)

### 2. Template Method Pattern
- **DocumentationGenerator** orchestrates workflow
- Delegates language-specific logic to writers
- Consistent error handling across all languages

### 3. Facade Pattern
- **WatsonxClient** hides API complexity
- Simple interface: `generate_docstring(signature, body)`
- Handles authentication, retries, error handling

### 4. Command Pattern
- **DocItem** encapsulates insertion operation
- Supports undo via backup/restore
- Enables batch processing

## Error Handling Strategy

```mermaid
graph TD
    Start[Start Documentation Generation]
    CheckEnv{Environment Variables Set?}
    CheckEnv -->|No| ErrorEnv[Display Error Message & Exit]
    CheckEnv -->|Yes| Process[Process Files]
    
    Process --> CreateBackup[Create .bak Backup]
    CreateBackup --> Generate[Generate Docstring via API]
    Generate -->|API Error| Retry{Retry Count < 3?}
    Retry -->|Yes| Generate
    Retry -->|No| Skip[Skip Item & Log Error]
    Generate -->|Success| Insert[Insert Docstring]
    
    Insert --> Validate{Syntax Valid?}
    Validate -->|No| Restore[Restore from Backup]
    Restore --> Skip
    Validate -->|Yes| Commit[Commit Changes]
    
    Skip --> NextItem{More Items?}
    Commit --> NextItem
    NextItem -->|Yes| Process
    NextItem -->|No| Report[Generate Report]
    Report --> End[End]
```

## Configuration Flow

```mermaid
graph LR
    A[.env File] --> B[Environment Variables]
    B --> C[WATSONX_API_KEY]
    B --> D[WATSONX_PROJECT_ID]
    B --> E[WATSONX_URL]
    
    C --> F[WatsonxClient]
    D --> F
    E --> F
    
    G[config.json] --> H[Scanner Config]
    H --> I[root_directory]
    H --> J[exclude_patterns]
    H --> K[include_extensions]
    
    F --> L[DocumentationGenerator]
    I --> L
    J --> L
    K --> L
```

## API Request/Response Flow

```mermaid
sequenceDiagram
    participant Writer as PythonWriter
    participant Client as WatsonxClient
    participant API as watsonx.ai API
    
    Writer->>Client: generate_docstring(signature, body)
    Client->>Client: Build prompt from template
    Client->>Client: Prepare API request
    
    Client->>API: POST /ml/v1/text/generation
    Note over Client,API: Headers: Authorization, Content-Type<br/>Body: model_id, input, parameters, project_id
    
    API-->>Client: 200 OK with generated text
    Client->>Client: Extract docstring from response
    Client->>Client: Validate no placeholders
    Client-->>Writer: Return formatted docstring
    
    Note over Writer: If API error, retry up to 3 times<br/>with exponential backoff
```

## File Modification Safety

```mermaid
graph TD
    A[Original File] --> B[Read Content]
    B --> C[Create .bak Backup]
    C --> D[Modify in Memory]
    D --> E[Write to .tmp File]
    E --> F{Syntax Valid?}
    F -->|Yes| G[Atomic Rename .tmp to Original]
    F -->|No| H[Delete .tmp]
    H --> I[Restore from .bak]
    G --> J[Keep .bak for Safety]
    I --> K[Log Error]
    J --> L[Success]
    K --> M[Failure]
```

## Coverage Calculation

```mermaid
graph LR
    A[Before Scan] --> B[Count Total Items]
    A --> C[Count Documented Items]
    B --> D[Calculate Coverage %]
    C --> D
    
    E[Generate Docs] --> F[Insert Docstrings]
    
    F --> G[After Scan]
    G --> H[Count Total Items]
    G --> I[Count Documented Items]
    H --> J[Calculate New Coverage %]
    I --> J
    
    D --> K[Compare]
    J --> K
    K --> L[Report Improvement]
```

## Implementation Phases

```mermaid
gantt
    title Implementation Timeline
    dateFormat YYYY-MM-DD
    section Phase 1: Foundation
    Create writers/ structure           :a1, 2026-05-03, 1d
    Implement BaseDocumentationWriter   :a2, after a1, 1d
    section Phase 2: API Integration
    Implement WatsonxClient            :b1, after a2, 1d
    Test API connectivity              :b2, after b1, 1d
    section Phase 3: Python Writer
    Implement PythonDocumentationWriter :c1, after b2, 1d
    Implement prompt engineering        :c2, after c1, 1d
    section Phase 4: File Operations
    Implement DocumentationInserter     :d1, after c2, 1d
    Implement backup/restore            :d2, after d1, 1d
    section Phase 5: Integration
    Implement DocumentationGenerator    :e1, after d2, 1d
    Integrate with scanner.py           :e2, after e1, 1d
    section Phase 6: Testing
    Unit tests                          :f1, after e2, 1d
    Integration tests                   :f2, after f1, 1d
```

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Documentation Coverage | 80%+ | Before/after scan comparison |
| Syntax Validity | 100% | All modified files must parse |
| No Placeholders | 100% | Validation check on all docstrings |
| API Success Rate | 95%+ | Successful API calls / total calls |
| Processing Speed | <1s per function | Time per docstring generation |
| Backup Success | 100% | All files backed up before modification |

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| API Failure | High | Retry logic, graceful degradation |
| Syntax Errors | High | Validation + automatic rollback |
| File Corruption | Critical | Mandatory backups, atomic operations |
| Poor Quality Docs | Medium | Prompt engineering, validation |
| Rate Limiting | Medium | Exponential backoff, batch processing |
| Missing Credentials | High | Clear error messages, .env.example |

## Next Steps

1. ✅ Review architecture and approve design
2. Switch to Code mode for implementation
3. Start with Phase 1: Foundation
4. Proceed sequentially through phases
5. Test thoroughly at each phase
6. Deploy and monitor