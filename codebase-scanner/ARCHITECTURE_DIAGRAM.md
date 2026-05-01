# Architecture Diagram: Documentation Writer System

## System Overview

```mermaid
graph TB
    subgraph "User Interface"
        CLI[scanner.py CLI]
    end
    
    subgraph "Core Orchestration"
        DG[DocumentationGenerator]
        Scanner[Codebase Scanner]
    end
    
    subgraph "Writers Module"
        BW[BaseDocumentationWriter]
        PW[PythonWriter]
        JW[JavaScriptWriter]
        JVW[JavaWriter]
        CW[CppWriter]
    end
    
    subgraph "File Operations"
        DI[DocumentationInserter]
        Backup[Backup Manager]
        Validator[Syntax Validator]
    end
    
    subgraph "Parsers"
        PP[PythonParser]
        JP[JavaScriptParser]
        JVP[JavaParser]
        CP[CppParser]
    end
    
    subgraph "Data Storage"
        JSON[Scan Results JSON]
        Files[Source Files]
    end
    
    CLI -->|--write-docs| DG
    CLI -->|scan| Scanner
    Scanner -->|extract metadata| PP
    Scanner -->|extract metadata| JP
    Scanner -->|extract metadata| JVP
    Scanner -->|extract metadata| CP
    Scanner -->|save results| JSON
    
    DG -->|load results| JSON
    DG -->|get writer| BW
    BW -.implements.- PW
    BW -.implements.- JW
    BW -.implements.- JVW
    BW -.implements.- CW
    
    DG -->|insert docs| DI
    DI -->|create backup| Backup
    DI -->|validate| Validator
    DI -->|modify| Files
    
    PW -->|generate| DI
    JW -->|generate| DI
    JVW -->|generate| DI
    CW -->|generate| DI
    
    DG -->|re-scan| Scanner
```

## Data Flow Diagram

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant Scanner
    participant DocGen
    participant Writer
    participant Inserter
    participant Files
    
    User->>CLI: python scanner.py --write-docs
    CLI->>Scanner: scan_codebase()
    Scanner->>Files: read source files
    Files-->>Scanner: file content
    Scanner->>Scanner: parse & analyze
    Scanner-->>CLI: scan_results.json
    
    CLI->>DocGen: generate_documentation()
    DocGen->>DocGen: load scan results
    DocGen->>DocGen: filter undocumented items
    
    loop For each file
        DocGen->>Writer: generate_function_doc()
        Writer-->>DocGen: documentation string
        DocGen->>Inserter: insert_documentation()
        Inserter->>Files: create backup
        Inserter->>Files: modify source
        Inserter->>Inserter: validate syntax
        alt Syntax Valid
            Inserter-->>DocGen: success
        else Syntax Invalid
            Inserter->>Files: restore backup
            Inserter-->>DocGen: error
        end
    end
    
    DocGen->>Scanner: re-scan for coverage
    Scanner-->>DocGen: updated coverage
    DocGen-->>CLI: generation report
    CLI-->>User: display results
```

## Component Interaction Matrix

| Component | Depends On | Provides To | Data Exchange |
|-----------|-----------|-------------|---------------|
| CLI | Scanner, DocGen | User | Commands, Results |
| Scanner | Parsers, Formatters | CLI, DocGen | Scan Results JSON |
| DocGen | Writers, Inserter | CLI | Generation Report |
| BaseWriter | - | Language Writers | Abstract Interface |
| PythonWriter | BaseWriter | DocGen | Python Docstrings |
| JavaScriptWriter | BaseWriter | DocGen | JSDoc Comments |
| JavaWriter | BaseWriter | DocGen | Javadoc Comments |
| CppWriter | BaseWriter | DocGen | Doxygen Comments |
| Inserter | Validator, Backup | DocGen | File Modifications |
| Parsers | - | Scanner | Metadata Extraction |

## Module Dependencies

```mermaid
graph LR
    subgraph "writers/"
        base[base_writer.py]
        python[python_writer.py]
        js[javascript_writer.py]
        java[java_writer.py]
        cpp[cpp_writer.py]
        inserter[doc_inserter.py]
    end
    
    subgraph "core/"
        docgen[doc_generator.py]
        extractor[extractor.py]
        walker[walker.py]
        detector[detector.py]
    end
    
    subgraph "parsers/"
        pparser[python_parser.py]
        jparser[javascript_parser.py]
        jvparser[java_parser.py]
        cparser[cpp_parser.py]
    end
    
    python --> base
    js --> base
    java --> base
    cpp --> base
    
    docgen --> python
    docgen --> js
    docgen --> java
    docgen --> cpp
    docgen --> inserter
    
    extractor --> pparser
    extractor --> jparser
    extractor --> jvparser
    extractor --> cparser
    extractor --> detector
```

## File Structure

```
codebase-scanner/
├── scanner.py                    # Main CLI entry point (MODIFIED)
├── config.json                   # Configuration (EXTENDED)
│
├── core/
│   ├── __init__.py
│   ├── walker.py                 # Directory traversal
│   ├── detector.py               # Language detection
│   ├── extractor.py              # Metadata extraction
│   └── doc_generator.py          # NEW: Documentation orchestrator
│
├── parsers/
│   ├── __init__.py
│   ├── base_parser.py            # Parser base class
│   ├── python_parser.py          # Python AST parser
│   ├── javascript_parser.py      # JS/TS regex parser
│   ├── java_parser.py            # Java regex parser
│   └── cpp_parser.py             # C/C++ regex parser
│
├── writers/                      # NEW: Documentation writers
│   ├── __init__.py
│   ├── base_writer.py            # Abstract base writer
│   ├── python_writer.py          # Google-style docstrings
│   ├── javascript_writer.py      # JSDoc comments
│   ├── java_writer.py            # Javadoc comments
│   ├── cpp_writer.py             # Doxygen comments
│   └── doc_inserter.py           # Safe file modification
│
├── formatters/
│   ├── __init__.py
│   ├── json_formatter.py         # JSON output
│   └── markdown_formatter.py     # Markdown output
│
├── utils/
│   ├── __init__.py
│   ├── logger.py                 # Logging utilities
│   └── filters.py                # File filtering
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_python_parser.py
│   ├── test_detector.py
│   ├── test_filters.py
│   ├── test_python_writer.py     # NEW: Writer tests
│   ├── test_javascript_writer.py # NEW
│   ├── test_java_writer.py       # NEW
│   ├── test_cpp_writer.py        # NEW
│   └── test_doc_inserter.py      # NEW
│
└── output/
    ├── documentation.json        # Scan results
    └── documentation.md          # Markdown report
```

## State Transitions

```mermaid
stateDiagram-v2
    [*] --> Scanning: User runs scanner
    Scanning --> ScanComplete: Files analyzed
    ScanComplete --> CheckFlag: Check --write-docs
    
    CheckFlag --> GeneratingDocs: Flag set
    CheckFlag --> [*]: Flag not set
    
    GeneratingDocs --> LoadingResults: Load scan JSON
    LoadingResults --> FilteringItems: Parse results
    FilteringItems --> ProcessingFiles: Get undocumented items
    
    ProcessingFiles --> GeneratingDoc: For each item
    GeneratingDoc --> InsertingDoc: Doc generated
    InsertingDoc --> ValidatingSyntax: Doc inserted
    
    ValidatingSyntax --> Success: Syntax valid
    ValidatingSyntax --> RestoreBackup: Syntax invalid
    RestoreBackup --> LogError: Backup restored
    
    Success --> ProcessingFiles: More items
    LogError --> ProcessingFiles: More items
    
    ProcessingFiles --> Rescanning: All items processed
    Rescanning --> GeneratingReport: Coverage calculated
    GeneratingReport --> [*]: Report displayed
```

## Error Handling Flow

```mermaid
graph TD
    Start[Start Documentation Generation]
    Start --> CreateBackup{Create Backup?}
    
    CreateBackup -->|Success| ReadFile[Read Source File]
    CreateBackup -->|Fail| BackupError[Log Backup Error]
    BackupError --> Skip[Skip File]
    
    ReadFile -->|Success| GenerateDocs[Generate Documentation]
    ReadFile -->|Fail| ReadError[Log Read Error]
    ReadError --> Skip
    
    GenerateDocs --> InsertDocs[Insert Documentation]
    InsertDocs --> WriteTempFile[Write to Temp File]
    
    WriteTempFile -->|Success| ValidateSyntax{Validate Syntax?}
    WriteTempFile -->|Fail| WriteError[Log Write Error]
    WriteError --> RestoreBackup[Restore from Backup]
    
    ValidateSyntax -->|Valid| AtomicReplace[Atomic File Replace]
    ValidateSyntax -->|Invalid| SyntaxError[Log Syntax Error]
    SyntaxError --> RestoreBackup
    
    AtomicReplace -->|Success| Success[Mark Success]
    AtomicReplace -->|Fail| ReplaceError[Log Replace Error]
    ReplaceError --> RestoreBackup
    
    RestoreBackup --> Skip
    Success --> Continue[Continue to Next File]
    Skip --> Continue
    Continue --> End[End]
```

## Performance Optimization Strategy

```mermaid
graph LR
    subgraph "Input"
        Files[Source Files]
    end
    
    subgraph "Optimization Layers"
        Cache[AST Cache]
        Batch[Batch Processor]
        Parallel[Parallel Workers]
    end
    
    subgraph "Processing"
        Parse[Parse Files]
        Generate[Generate Docs]
        Insert[Insert Docs]
    end
    
    subgraph "Output"
        Modified[Modified Files]
        Report[Coverage Report]
    end
    
    Files --> Cache
    Cache --> Batch
    Batch --> Parallel
    
    Parallel --> Parse
    Parse --> Generate
    Generate --> Insert
    
    Insert --> Modified
    Insert --> Report
```

## Security Boundaries

```mermaid
graph TB
    subgraph "Trusted Zone"
        Scanner[Scanner Core]
        Writers[Documentation Writers]
    end
    
    subgraph "Validation Layer"
        PathValidator[Path Validator]
        SyntaxValidator[Syntax Validator]
        ContentValidator[Content Validator]
    end
    
    subgraph "Untrusted Zone"
        UserInput[User Input]
        SourceFiles[Source Files]
    end
    
    UserInput -->|validate| PathValidator
    PathValidator -->|sanitized paths| Scanner
    
    SourceFiles -->|read| Scanner
    Scanner -->|parse| Writers
    Writers -->|generate| ContentValidator
    ContentValidator -->|validate| SyntaxValidator
    SyntaxValidator -->|safe content| SourceFiles
```

## Deployment Architecture

```mermaid
graph TB
    subgraph "Development Environment"
        Dev[Developer Machine]
        DevFiles[Local Source Files]
    end
    
    subgraph "CI/CD Pipeline"
        CI[CI Server]
        PreCommit[Pre-commit Hook]
        BuildStep[Build Step]
    end
    
    subgraph "Production"
        Prod[Production Codebase]
        Docs[Generated Documentation]
    end
    
    Dev -->|commit| PreCommit
    PreCommit -->|run scanner| DevFiles
    PreCommit -->|--write-docs| DevFiles
    
    PreCommit -->|push| CI
    CI -->|scan| BuildStep
    BuildStep -->|validate coverage| CI
    
    CI -->|deploy| Prod
    Prod -->|generate| Docs
```

## Key Design Principles

1. **Separation of Concerns**: Each module has a single, well-defined responsibility
2. **Language Agnostic Core**: Core logic independent of specific languages
3. **Safe File Operations**: Always backup, validate, and use atomic operations
4. **Extensibility**: Easy to add new language support via inheritance
5. **Error Resilience**: Graceful degradation with detailed error reporting
6. **Performance**: Batch processing and caching for large codebases
7. **Security**: Input validation and sandboxed execution
8. **Testability**: Clear interfaces and dependency injection

## Extension Points

To add support for a new language:

1. Create new parser in `parsers/` (inherit from `BaseParser`)
2. Create new writer in `writers/` (inherit from `BaseDocumentationWriter`)
3. Add language mapping in `core/extractor.py`
4. Add syntax validator in `writers/doc_inserter.py`
5. Add configuration in `config.json`
6. Create unit tests in `tests/`

Example for adding Rust support:

```python
# parsers/rust_parser.py
class RustParser(BaseParser):
    def parse(self) -> Dict[str, Any]:
        # Implement Rust-specific parsing
        pass

# writers/rust_writer.py
class RustDocumentationWriter(BaseDocumentationWriter):
    def get_doc_start_marker(self) -> str:
        return '///'
    
    def generate_function_doc(self, func_info: Dict) -> str:
        # Generate Rust doc comments
        pass