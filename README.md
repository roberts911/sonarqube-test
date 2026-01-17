# SonarQube Demo Project

Ten projekt zawiera celowo wprowadzone błędy i problemy w kodzie Python, aby zademonstrować możliwości SonarQube.

## Typy problemów w kodzie:

### 🔴 Security Issues (Problemy bezpieczeństwa):
- Hard-coded credentials (hasła w kodzie)
- SQL Injection
- Command Injection
- Insecure deserialization (pickle)
- Weak cryptography (MD5)
- Unsafe eval() usage

### 🟡 Bugs (Błędy):
- Mutable default arguments
- Division by zero risk
- Broad exception handling
- Comparing None with ==
- Modifying list while iterating

### 🟢 Code Smells:
- Unused variables
- Dead code
- Code duplication
- Too many parameters
- High cognitive complexity
- Too many return statements
- Magic numbers
- Print statements instead of logging
- Too many local variables

### Oczekiwane wyniki:

SonarQube powinien wykryć:
- **20+** Security Hotspots
- **15+** Bugs
- **25+** Code Smells
- **High** Cognitive Complexity
- **Duplicated** Code Blocks

### Użyte technologie:
- Python 3.8+
- SonarQube/SonarCloud
