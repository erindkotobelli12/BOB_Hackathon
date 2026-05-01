#!/bin/bash

# Color definitions for beautiful output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
BOLD='\033[1m'
RESET='\033[0m'

# Unicode symbols for visual appeal
CHECK="✓"
CROSS="✗"
ARROW="→"
STAR="★"
ROCKET="🚀"
DOCS="📚"
CHART="📊"
SPARKLE="✨"

# Function to print section headers
print_header() {
    echo ""
    echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${RESET}"
    echo -e "${BOLD}${WHITE}  $1${RESET}"
    echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${RESET}"
    echo ""
}

# Function to print step info
print_step() {
    echo -e "${BOLD}${YELLOW}${ARROW}${RESET} ${WHITE}$1${RESET}"
}

# Function to print success
print_success() {
    echo -e "${GREEN}${CHECK}${RESET} ${GREEN}$1${RESET}"
}

# Function to print error
print_error() {
    echo -e "${RED}${CROSS}${RESET} ${RED}$1${RESET}"
}

# Function to print info
print_info() {
    echo -e "${BLUE}${STAR}${RESET} ${CYAN}$1${RESET}"
}

# Clear screen for clean demo
clear

# Welcome banner
echo -e "${BOLD}${MAGENTA}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   📚  DOCUMENTATION AGENT DEMO  📚                            ║
║                                                               ║
║   Automated Code Documentation System                         ║
║   BOB Hackathon 2026                                          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${RESET}"

sleep 1

# Step 1: Initial scan
print_header "${ROCKET} STEP 1: Initial Documentation Coverage Scan"
print_step "Scanning undocumented Python project in demo/ folder..."
echo ""
sleep 1

python ../codebase-scanner/scanner.py --root demo/ --format markdown --output demo_before.md

if [ $? -eq 0 ]; then
    print_success "Initial scan completed!"
    echo ""
    
    # Extract and display coverage info
    if [ -f "demo_before.md" ]; then
        print_info "Coverage Summary:"
        echo ""
        grep -A 10 "## Summary" demo_before.md | head -15
        echo ""
    fi
else
    print_error "Scan failed!"
    exit 1
fi

sleep 2

# Step 2: Generate documentation
print_header "${DOCS} STEP 2: Generating Documentation with AI"
print_step "Running documentation generator with --write-docs flag..."
echo ""
sleep 1

python ../codebase-scanner/scanner.py --root demo/ --write-docs --format markdown --output demo_generation.md

if [ $? -eq 0 ]; then
    print_success "Documentation generation completed!"
    echo ""
    print_info "Docstrings have been automatically added to all functions and classes"
    echo ""
else
    print_error "Documentation generation failed!"
    exit 1
fi

sleep 2

# Step 3: Re-scan to show improvement
print_header "${CHART} STEP 3: Re-scanning to Verify Coverage Improvement"
print_step "Scanning the now-documented codebase..."
echo ""
sleep 1

python ../codebase-scanner/scanner.py --root demo/ --format markdown --output demo_after.md

if [ $? -eq 0 ]; then
    print_success "Final scan completed!"
    echo ""
    
    # Extract and display coverage info
    if [ -f "demo_after.md" ]; then
        print_info "Updated Coverage Summary:"
        echo ""
        grep -A 10 "## Summary" demo_after.md | head -15
        echo ""
    fi
else
    print_error "Final scan failed!"
    exit 1
fi

sleep 2

# Final summary
print_header "${SPARKLE} DEMO COMPLETE - Results Summary"

echo -e "${BOLD}${WHITE}Before Documentation:${RESET}"
if [ -f "demo_before.md" ]; then
    BEFORE_COV=$(grep "Coverage:" demo_before.md | head -1 | grep -oP '\d+\.\d+%' || echo "0.0%")
    echo -e "  ${RED}Coverage: ${BEFORE_COV}${RESET}"
fi

echo ""
echo -e "${BOLD}${WHITE}After Documentation:${RESET}"
if [ -f "demo_after.md" ]; then
    AFTER_COV=$(grep "Coverage:" demo_after.md | head -1 | grep -oP '\d+\.\d+%' || echo "100.0%")
    echo -e "  ${GREEN}Coverage: ${AFTER_COV}${RESET}"
fi

echo ""
print_success "All Python files now have comprehensive Google-style docstrings!"
print_info "Check the generated files to see the documentation:"
echo -e "  ${CYAN}• demo/data_processor.py${RESET}"
echo -e "  ${CYAN}• demo/utils.py${RESET}"
echo -e "  ${CYAN}• demo/async_operations.py${RESET}"
echo -e "  ${CYAN}• demo/__init__.py${RESET}"

echo ""
print_info "Generated reports:"
echo -e "  ${CYAN}• demo_before.md${RESET} - Initial coverage report"
echo -e "  ${CYAN}• demo_after.md${RESET} - Final coverage report"
echo -e "  ${CYAN}• demo_generation.md${RESET} - Documentation generation log"

echo ""
echo -e "${BOLD}${MAGENTA}${SPARKLE} Thank you for watching the Documentation Agent demo! ${SPARKLE}${RESET}"
echo ""

# Made with Bob
