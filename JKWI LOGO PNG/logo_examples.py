#!/usr/bin/env python3
"""
JKWI Logo Manager - Usage Examples
=================================

This script demonstrates how to use the JKWI Logo Management System
for automated systems, web applications, and other platforms.
"""

from logo_manager import JKWILogoManager, LogoCategory


def demonstrate_basic_usage():
    """Demonstrate basic logo manager functionality."""
    print("=== Basic Usage Examples ===\n")
    
    # Initialize the manager
    manager = JKWILogoManager()
    
    # Get company logo (main variant)
    print("1. Getting main company logo:")
    company_logo = manager.get_company_logo("main")
    if company_logo:
        print(f"   Name: {company_logo.name}")
        print(f"   URL: {company_logo.url}")
        print(f"   Description: {company_logo.description}")
    print()
    
    # Get company logo (white variant)
    print("2. Getting white company logo:")
    company_logo_white = manager.get_company_logo("white")
    if company_logo_white:
        print(f"   Name: {company_logo_white.name}")
        print(f"   URL: {company_logo_white.url}")
    print()
    
    # Get all division logos
    print("3. Getting all division logos:")
    division_logos = manager.get_logos_by_category("division")
    for i, logo in enumerate(division_logos, 1):
        print(f"   {i}. {logo.name} - {logo.description}")
    print()


def demonstrate_search_functionality():
    """Demonstrate search capabilities."""
    print("=== Search Functionality ===\n")
    
    manager = JKWILogoManager()
    
    # Search for white logos
    print("1. Searching for 'white' logos:")
    white_logos = manager.search_logos("white")
    for logo in white_logos[:5]:  # Show first 5
        print(f"   - {logo.name}")
    print(f"   Total white logos: {len(white_logos)}")
    print()
    
    # Search for investment-related logos
    print("2. Searching for 'investment' logos:")
    investment_logos = manager.search_logos("investment")
    for logo in investment_logos[:5]:  # Show first 5
        print(f"   - {logo.name}")
    print(f"   Total investment logos: {len(investment_logos)}")
    print()


def demonstrate_category_filtering():
    """Demonstrate category-based filtering."""
    print("=== Category Filtering ===\n")
    
    manager = JKWILogoManager()
    
    # Get logos by each category
    for category in ["company", "division", "partners", "investors"]:
        logos = manager.get_logos_by_category(category)
        print(f"{category.title()} logos ({len(logos)}):")
        for logo in logos[:3]:  # Show first 3
            print(f"   - {logo.name}")
        if len(logos) > 3:
            print(f"   ... and {len(logos) - 3} more")
        print()


def demonstrate_json_export():
    """Demonstrate JSON export functionality."""
    print("=== JSON Export ===\n")
    
    manager = JKWILogoManager()
    
    # Export all data as JSON
    json_data = manager.to_json(pretty=True)
    
    # Show a snippet of the JSON
    lines = json_data.split('\n')
    print("JSON export sample (first 20 lines):")
    for line in lines[:20]:
        print(line)
    print("...")
    print(f"Total JSON size: {len(json_data)} characters")
    print()


def demonstrate_web_integration():
    """Demonstrate how to use for web applications."""
    print("=== Web Integration Examples ===\n")
    
    manager = JKWILogoManager()
    
    # Example 1: Get logo for a specific page
    print("1. Logo for company homepage:")
    main_logo = manager.get_company_logo("main")
    if main_logo:
        print(f'   <img src="{main_logo.url}" alt="{main_logo.description}">')
    print()
    
    # Example 2: Generate navigation logos
    print("2. Division navigation logos:")
    division_logos = manager.get_logos_by_category("division")
    for logo in division_logos[:3]:  # Show first 3
        print(f'   <a href="/{logo.name}"><img src="{logo.url}" alt="{logo.description}"></a>')
    print()
    
    # Example 3: Partner logos for footer
    print("3. Partner logos for footer:")
    partner_logos = manager.get_logos_by_category("partners")
    for logo in partner_logos[:3]:  # Show first 3
        print(f'   <img src="{logo.url}" alt="{logo.description}" style="height: 40px;">')
    print()


def demonstrate_api_responses():
    """Demonstrate API-style responses."""
    print("=== API Response Examples ===\n")
    
    manager = JKWILogoManager()
    
    # Example API response for getting a specific logo
    print("1. API Response - Get specific logo:")
    logo = manager.get_logo_by_name("jk_winners_investment_main")
    if logo:
        response = {
            "status": "success",
            "data": logo.to_dict()
        }
        print(f"   {response}")
    print()
    
    # Example API response for category search
    print("2. API Response - Get category logos:")
    logos = manager.get_logos_by_category("company")
    response = {
        "status": "success",
        "count": len(logos),
        "data": [logo.to_dict() for logo in logos]
    }
    print(f"   Status: {response['status']}")
    print(f"   Count: {response['count']}")
    print(f"   Data: [Logo objects...]")
    print()


def main():
    """Run all demonstration examples."""
    print("JKWI Logo Manager - Usage Examples")
    print("=" * 50)
    print()
    
    demonstrate_basic_usage()
    demonstrate_search_functionality()
    demonstrate_category_filtering()
    demonstrate_json_export()
    demonstrate_web_integration()
    demonstrate_api_responses()
    
    print("=== Summary ===")
    manager = JKWILogoManager()
    print(f"Total logos available: {len(manager.get_all_logos())}")
    print(f"Categories: {', '.join(manager.get_categories())}")
    print(f"Repository: https://github.com/jkwinnersinvestment/JKWI-WEB")
    print("\nFor more information, see logo_config.json")


if __name__ == "__main__":
    main()
