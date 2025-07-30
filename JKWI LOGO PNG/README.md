# JKWI Logo Management System

A comprehensive, automated logo management system for JK Winners Investment that provides structured access to all company, division, partner, and investor logos.

## Overview

This system provides a readable, automated solution for accessing JKWI logos across all platforms. It includes:

- **Structured logo registry** with metadata
- **Category-based organization** (Company, Division, Partners, Investors)
- **Search functionality** for finding specific logos
- **Multiple export formats** (JSON, HTML)
- **Web-ready URLs** for direct integration
- **Color variant support** (main and white versions)

## Repository Structure

```
JKWI-WEB/
├── logo_manager.py       # Main logo management system
├── logo_examples.py      # Usage examples and demonstrations
├── logo_config.json      # Configuration and API documentation
├── requirements.txt      # Python dependencies
└── README.md            # This documentation
```

## Quick Start

### 1. Installation

```bash
# Install Python dependencies
pip install -r requirements.txt
```

### 2. Basic Usage

```python
from logo_manager import JKWILogoManager

# Initialize the manager
manager = JKWILogoManager()

# Get main company logo
company_logo = manager.get_company_logo("main")
print(f"Logo URL: {company_logo.url}")

# Get all division logos
division_logos = manager.get_logos_by_category("division")

# Search for specific logos
white_logos = manager.search_logos("white")
```

### 3. Run Examples

```bash
python logo_examples.py
```

## Available Logo Categories

### 1. Company Logos
- JK Winners Investment (main and white variants)

### 2. Division Logos
- JKWI Foundation
- JKWI Innovation Hub  
- JKWI Properties
- JKWI Ventures

### 3. Partners Logos
- Africa Investment and Trade Expo
- Black Owned Business Network
- BNB Exchange
- Corporate Bridge
- Investment Bridge
- JK Winners Investment Platform

### 4. Investors Logos
- JKWI Angel Investors
- JKWI Crowd Funding
- JKWI Fund Managers
- JKWI Investment Club
- JKWI Portfolio
- JKWI Private Equity
- JKWI Seed Fund
- JKWI Venture Capital

## API Reference

### Core Methods

#### `get_logo_by_name(name: str) -> Optional[LogoInfo]`
Get a specific logo by its unique name.

```python
logo = manager.get_logo_by_name("jk_winners_investment_main")
```

#### `get_logos_by_category(category: str) -> List[LogoInfo]`
Get all logos in a specific category.

```python
# Available categories: "company", "division", "partners", "investors"
logos = manager.get_logos_by_category("division")
```

#### `get_company_logo(variant: str = "main") -> Optional[LogoInfo]`
Get the main company logo with optional variant.

```python
main_logo = manager.get_company_logo("main")
white_logo = manager.get_company_logo("white")
```

#### `search_logos(query: str) -> List[LogoInfo]`
Search logos by name, description, or filename.

```python
results = manager.search_logos("investment")
```

#### `get_all_logos() -> List[LogoInfo]`
Get all available logos.

```python
all_logos = manager.get_all_logos()
```

### Export Methods

#### `to_json(pretty: bool = True) -> str`
Export all logo data as JSON.

```python
json_data = manager.to_json(pretty=True)
```

#### `generate_html_gallery() -> str`
Generate an HTML gallery of all logos.

```python
html_gallery = manager.generate_html_gallery()
```

## LogoInfo Object Structure

Each logo is represented by a `LogoInfo` object with the following properties:

```python
{
    "name": "jk_winners_investment_main",
    "category": "company",
    "filename": "JK WINNERS INVESTMENT LOGO.png",
    "url": "https://raw.githubusercontent.com/jkwinnersinvestment/JKWI-WEB/main/JKWI%20LOGO%20PNG/JK%20WINNERS%20INVESTMENT%20LOGO.png",
    "description": "Main company logo for JK Winners Investment",
    "size_hint": null,
    "color_variant": "full_color"
}
```

## Web Integration Examples

### HTML Integration
```html
<!-- Company logo -->
<img src="https://raw.githubusercontent.com/jkwinnersinvestment/JKWI-WEB/main/JKWI%20LOGO%20PNG/JK%20WINNERS%20INVESTMENT%20LOGO.png" 
     alt="JK Winners Investment Logo">

<!-- Division logos -->
<img src="https://raw.githubusercontent.com/jkwinnersinvestment/JKWI-WEB/main/JKWI%20LOGO%20PNG/JKWI%20FOUNDATION%20LOGO.png" 
     alt="JKWI Foundation Logo">
```

### JavaScript/API Integration
```javascript
// Fetch logo data
const response = await fetch('/api/logos/company');
const logos = await response.json();

// Use logo in web app
document.getElementById('company-logo').src = logos[0].url;
```

### CSS Background Integration
```css
.company-logo {
    background-image: url('https://raw.githubusercontent.com/jkwinnersinvestment/JKWI-WEB/main/JKWI%20LOGO%20PNG/JK%20WINNERS%20INVESTMENT%20LOGO.png');
    background-size: contain;
    background-repeat: no-repeat;
}
```

## Automated System Integration

### Python Applications
```python
from logo_manager import JKWILogoManager

class WebsiteBuilder:
    def __init__(self):
        self.logo_manager = JKWILogoManager()
    
    def get_header_logo(self):
        return self.logo_manager.get_company_logo("main").url
    
    def get_footer_partners(self):
        return [logo.url for logo in self.logo_manager.get_logos_by_category("partners")]
```

### REST API Integration
```python
from flask import Flask, jsonify
from logo_manager import JKWILogoManager

app = Flask(__name__)
manager = JKWILogoManager()

@app.route('/api/logos/<category>')
def get_logos_by_category(category):
    logos = manager.get_logos_by_category(category)
    return jsonify([logo.to_dict() for logo in logos])
```

### Configuration Management
```python
import json
from logo_manager import JKWILogoManager

# Generate configuration file for other systems
manager = JKWILogoManager()
config = {
    "logos": {logo.name: logo.url for logo in manager.get_all_logos()},
    "categories": {cat: [logo.name for logo in manager.get_logos_by_category(cat)] 
                   for cat in manager.get_categories()}
}

with open('logo_config.json', 'w') as f:
    json.dump(config, f, indent=2)
```

## Platform Compatibility

This system is designed to work across multiple platforms:

- **Web Applications**: Direct URL access, JSON API responses
- **Mobile Apps**: RESTful API integration, JSON data format
- **Desktop Applications**: Python library import, local file access
- **CI/CD Pipelines**: Automated logo deployment and validation
- **Content Management**: Dynamic logo selection and integration
- **Documentation**: Automated logo insertion in docs and presentations

## Error Handling

The system includes robust error handling:

```python
# Safe logo retrieval
logo = manager.get_logo_by_name("unknown_logo")
if logo:
    print(f"Logo found: {logo.url}")
else:
    print("Logo not found, using default")

# Category validation
logos = manager.get_logos_by_category("invalid_category")
# Returns empty list for invalid categories
```

## Contributing

When adding new logos to the repository:

1. Add the logo file to the `/JKWI LOGO PNG/` directory
2. Update the `LOGO_REGISTRY` in `logo_manager.py`
3. Follow the naming convention: descriptive names with category prefix
4. Include both main and white variants when applicable
5. Update this README with new logo information

## License

This logo management system is part of the JKWI-WEB repository and follows the same licensing terms.

## Repository Information

- **Repository**: https://github.com/jkwinnersinvestment/JKWI-WEB
- **Logo Directory**: `/JKWI LOGO PNG/`
- **Base URL**: https://raw.githubusercontent.com/jkwinnersinvestment/JKWI-WEB/main/JKWI%20LOGO%20PNG/
- **Version**: 1.0.0
- **Last Updated**: July 31, 2025

## Support

For issues, questions, or contributions, please use the GitHub repository's issue tracker or contact the JKWI development team.
