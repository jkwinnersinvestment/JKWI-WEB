#!/usr/bin/env python3
"""
JKWI Logo Management System
==========================

A comprehensive script to manage and provide relevant logos for JK Winners Investment.
This script is designed to be readable by automated systems and all platforms.

Repository: https://github.com/jkwinnersinvestment/JKWI-WEB
Logo Directory: /JKWI%20LOGO%20PNG/

Author: JKWI Development Team
Version: 1.0.0
Date: July 31, 2025
"""

import json
import os
import re
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, asdict
from enum import Enum


class LogoCategory(Enum):
    """Enumeration of logo categories available in the repository."""
    COMPANY = "company"
    DIVISION = "division"
    PARTNERS = "partners"
    INVESTORS = "investors"


class LogoFormat(Enum):
    """Supported logo formats."""
    PNG = "png"
    JPG = "jpg"
    JPEG = "jpeg"
    SVG = "svg"
    WEBP = "webp"


@dataclass
class LogoInfo:
    """Data class representing logo information."""
    name: str
    category: LogoCategory
    filename: str
    url: str
    description: str
    size_hint: Optional[str] = None
    color_variant: Optional[str] = None
    
    def to_dict(self) -> Dict:
        """Convert logo info to dictionary format."""
        result = asdict(self)
        result['category'] = self.category.value
        return result


class JKWILogoManager:
    """
    Main logo management class for JK Winners Investment.
    
    This class provides methods to:
    - Retrieve logos by category, name, or type
    - Generate logo URLs
    - Provide logo metadata
    - Support automated systems with structured data
    """
    
    # Base GitHub repository URL
    BASE_URL = "https://raw.githubusercontent.com/jkwinnersinvestment/JKWI-WEB/main/JKWI%20LOGO%20PNG"
    
    # Logo registry based on the repository structure
    LOGO_REGISTRY = [
        # Company Logos
        LogoInfo(
            name="jk_winners_investment_main",
            category=LogoCategory.COMPANY,
            filename="JK WINNERS INVESTMENT LOGO.png",
            url=f"{BASE_URL}/JK%20WINNERS%20INVESTMENT%20LOGO.png",
            description="Main company logo for JK Winners Investment",
            color_variant="full_color"
        ),
        LogoInfo(
            name="jk_winners_investment_white",
            category=LogoCategory.COMPANY,
            filename="JK WINNERS INVESTMENT LOGO WHITE.png",
            url=f"{BASE_URL}/JK%20WINNERS%20INVESTMENT%20LOGO%20WHITE.png",
            description="White variant of JK Winners Investment logo",
            color_variant="white"
        ),
        
        # Division Logos
        LogoInfo(
            name="jkwi_foundation",
            category=LogoCategory.DIVISION,
            filename="JKWI FOUNDATION LOGO.png",
            url=f"{BASE_URL}/JKWI%20FOUNDATION%20LOGO.png",
            description="JKWI Foundation division logo"
        ),
        LogoInfo(
            name="jkwi_foundation_white",
            category=LogoCategory.DIVISION,
            filename="JKWI FOUNDATION LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20FOUNDATION%20LOGO%20WHITE.png",
            description="White variant of JKWI Foundation logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jkwi_innovation_hub",
            category=LogoCategory.DIVISION,
            filename="JKWI INNOVATION HUB LOGO.png",
            url=f"{BASE_URL}/JKWI%20INNOVATION%20HUB%20LOGO.png",
            description="JKWI Innovation Hub division logo"
        ),
        LogoInfo(
            name="jkwi_innovation_hub_white",
            category=LogoCategory.DIVISION,
            filename="JKWI INNOVATION HUB LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20INNOVATION%20HUB%20LOGO%20WHITE.png",
            description="White variant of JKWI Innovation Hub logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jkwi_properties",
            category=LogoCategory.DIVISION,
            filename="JKWI PROPERTIES LOGO.png",
            url=f"{BASE_URL}/JKWI%20PROPERTIES%20LOGO.png",
            description="JKWI Properties division logo"
        ),
        LogoInfo(
            name="jkwi_properties_white",
            category=LogoCategory.DIVISION,
            filename="JKWI PROPERTIES LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20PROPERTIES%20LOGO%20WHITE.png",
            description="White variant of JKWI Properties logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jkwi_ventures",
            category=LogoCategory.DIVISION,
            filename="JKWI VENTURES LOGO.png",
            url=f"{BASE_URL}/JKWI%20VENTURES%20LOGO.png",
            description="JKWI Ventures division logo"
        ),
        LogoInfo(
            name="jkwi_ventures_white",
            category=LogoCategory.DIVISION,
            filename="JKWI VENTURES LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20VENTURES%20LOGO%20WHITE.png",
            description="White variant of JKWI Ventures logo",
            color_variant="white"
        ),
        
        # Partners Logos
        LogoInfo(
            name="africa_investment_trade_expo",
            category=LogoCategory.PARTNERS,
            filename="AFRICA INVESTMENT AND TRADE EXPO LOGO.png",
            url=f"{BASE_URL}/AFRICA%20INVESTMENT%20AND%20TRADE%20EXPO%20LOGO.png",
            description="Africa Investment and Trade Expo partner logo"
        ),
        LogoInfo(
            name="africa_investment_trade_expo_white",
            category=LogoCategory.PARTNERS,
            filename="AFRICA INVESTMENT AND TRADE EXPO LOGO WHITE.png",
            url=f"{BASE_URL}/AFRICA%20INVESTMENT%20AND%20TRADE%20EXPO%20LOGO%20WHITE.png",
            description="White variant of Africa Investment and Trade Expo logo",
            color_variant="white"
        ),
        LogoInfo(
            name="black_owned_business_network",
            category=LogoCategory.PARTNERS,
            filename="BLACK OWNED BUSINESS NETWORK LOGO.png",
            url=f"{BASE_URL}/BLACK%20OWNED%20BUSINESS%20NETWORK%20LOGO.png",
            description="Black Owned Business Network partner logo"
        ),
        LogoInfo(
            name="black_owned_business_network_white",
            category=LogoCategory.PARTNERS,
            filename="BLACK OWNED BUSINESS NETWORK LOGO WHITE.png",
            url=f"{BASE_URL}/BLACK%20OWNED%20BUSINESS%20NETWORK%20LOGO%20WHITE.png",
            description="White variant of Black Owned Business Network logo",
            color_variant="white"
        ),
        LogoInfo(
            name="bnb_exchange",
            category=LogoCategory.PARTNERS,
            filename="BNB EXCHANGE LOGO.png",
            url=f"{BASE_URL}/BNB%20EXCHANGE%20LOGO.png",
            description="BNB Exchange partner logo"
        ),
        LogoInfo(
            name="bnb_exchange_white",
            category=LogoCategory.PARTNERS,
            filename="BNB EXCHANGE LOGO WHITE.png",
            url=f"{BASE_URL}/BNB%20EXCHANGE%20LOGO%20WHITE.png",
            description="White variant of BNB Exchange logo",
            color_variant="white"
        ),
        LogoInfo(
            name="corporate_bridge",
            category=LogoCategory.PARTNERS,
            filename="CORPORATE BRIDGE LOGO.png",
            url=f"{BASE_URL}/CORPORATE%20BRIDGE%20LOGO.png",
            description="Corporate Bridge partner logo"
        ),
        LogoInfo(
            name="corporate_bridge_white",
            category=LogoCategory.PARTNERS,
            filename="CORPORATE BRIDGE LOGO WHITE.png",
            url=f"{BASE_URL}/CORPORATE%20BRIDGE%20LOGO%20WHITE.png",
            description="White variant of Corporate Bridge logo",
            color_variant="white"
        ),
        LogoInfo(
            name="investment_bridge",
            category=LogoCategory.PARTNERS,
            filename="INVESTMENT BRIDGE LOGO.png",
            url=f"{BASE_URL}/INVESTMENT%20BRIDGE%20LOGO.png",
            description="Investment Bridge partner logo"
        ),
        LogoInfo(
            name="investment_bridge_white",
            category=LogoCategory.PARTNERS,
            filename="INVESTMENT BRIDGE LOGO WHITE.png",
            url=f"{BASE_URL}/INVESTMENT%20BRIDGE%20LOGO%20WHITE.png",
            description="White variant of Investment Bridge logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jk_winners_investment_platform",
            category=LogoCategory.PARTNERS,
            filename="JK WINNERS INVESTMENT PLATFORM LOGO.png",
            url=f"{BASE_URL}/JK%20WINNERS%20INVESTMENT%20PLATFORM%20LOGO.png",
            description="JK Winners Investment Platform logo"
        ),
        LogoInfo(
            name="jk_winners_investment_platform_white",
            category=LogoCategory.PARTNERS,
            filename="JK WINNERS INVESTMENT PLATFORM LOGO WHITE.png",
            url=f"{BASE_URL}/JK%20WINNERS%20INVESTMENT%20PLATFORM%20LOGO%20WHITE.png",
            description="White variant of JK Winners Investment Platform logo",
            color_variant="white"
        ),
        
        # Investors Logos
        LogoInfo(
            name="jkwi_angel_investors",
            category=LogoCategory.INVESTORS,
            filename="JKWI ANGEL INVESTORS LOGO.png",
            url=f"{BASE_URL}/JKWI%20ANGEL%20INVESTORS%20LOGO.png",
            description="JKWI Angel Investors logo"
        ),
        LogoInfo(
            name="jkwi_angel_investors_white",
            category=LogoCategory.INVESTORS,
            filename="JKWI ANGEL INVESTORS LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20ANGEL%20INVESTORS%20LOGO%20WHITE.png",
            description="White variant of JKWI Angel Investors logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jkwi_crowd_funding",
            category=LogoCategory.INVESTORS,
            filename="JKWI CROWD FUNDING LOGO.png",
            url=f"{BASE_URL}/JKWI%20CROWD%20FUNDING%20LOGO.png",
            description="JKWI Crowd Funding logo"
        ),
        LogoInfo(
            name="jkwi_crowd_funding_white",
            category=LogoCategory.INVESTORS,
            filename="JKWI CROWD FUNDING LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20CROWD%20FUNDING%20LOGO%20WHITE.png",
            description="White variant of JKWI Crowd Funding logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jkwi_fund_managers",
            category=LogoCategory.INVESTORS,
            filename="JKWI FUND MANAGERS LOGO.png",
            url=f"{BASE_URL}/JKWI%20FUND%20MANAGERS%20LOGO.png",
            description="JKWI Fund Managers logo"
        ),
        LogoInfo(
            name="jkwi_fund_managers_white",
            category=LogoCategory.INVESTORS,
            filename="JKWI FUND MANAGERS LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20FUND%20MANAGERS%20LOGO%20WHITE.png",
            description="White variant of JKWI Fund Managers logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jkwi_investment_club",
            category=LogoCategory.INVESTORS,
            filename="JKWI INVESTMENT CLUB LOGO.png",
            url=f"{BASE_URL}/JKWI%20INVESTMENT%20CLUB%20LOGO.png",
            description="JKWI Investment Club logo"
        ),
        LogoInfo(
            name="jkwi_investment_club_white",
            category=LogoCategory.INVESTORS,
            filename="JKWI INVESTMENT CLUB LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20INVESTMENT%20CLUB%20LOGO%20WHITE.png",
            description="White variant of JKWI Investment Club logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jkwi_portfolio",
            category=LogoCategory.INVESTORS,
            filename="JKWI PORTFOLIO LOGO.png",
            url=f"{BASE_URL}/JKWI%20PORTFOLIO%20LOGO.png",
            description="JKWI Portfolio logo"
        ),
        LogoInfo(
            name="jkwi_portfolio_white",
            category=LogoCategory.INVESTORS,
            filename="JKWI PORTFOLIO LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20PORTFOLIO%20LOGO%20WHITE.png",
            description="White variant of JKWI Portfolio logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jkwi_private_equity",
            category=LogoCategory.INVESTORS,
            filename="JKWI PRIVATE EQUITY LOGO.png",
            url=f"{BASE_URL}/JKWI%20PRIVATE%20EQUITY%20LOGO.png",
            description="JKWI Private Equity logo"
        ),
        LogoInfo(
            name="jkwi_private_equity_white",
            category=LogoCategory.INVESTORS,
            filename="JKWI PRIVATE EQUITY LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20PRIVATE%20EQUITY%20LOGO%20WHITE.png",
            description="White variant of JKWI Private Equity logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jkwi_seed_fund",
            category=LogoCategory.INVESTORS,
            filename="JKWI SEED FUND LOGO.png",
            url=f"{BASE_URL}/JKWI%20SEED%20FUND%20LOGO.png",
            description="JKWI Seed Fund logo"
        ),
        LogoInfo(
            name="jkwi_seed_fund_white",
            category=LogoCategory.INVESTORS,
            filename="JKWI SEED FUND LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20SEED%20FUND%20LOGO%20WHITE.png",
            description="White variant of JKWI Seed Fund logo",
            color_variant="white"
        ),
        LogoInfo(
            name="jkwi_venture_capital",
            category=LogoCategory.INVESTORS,
            filename="JKWI VENTURE CAPITAL LOGO.png",
            url=f"{BASE_URL}/JKWI%20VENTURE%20CAPITAL%20LOGO.png",
            description="JKWI Venture Capital logo"
        ),
        LogoInfo(
            name="jkwi_venture_capital_white",
            category=LogoCategory.INVESTORS,
            filename="JKWI VENTURE CAPITAL LOGO WHITE.png",
            url=f"{BASE_URL}/JKWI%20VENTURE%20CAPITAL%20LOGO%20WHITE.png",
            description="White variant of JKWI Venture Capital logo",
            color_variant="white"
        )
    ]
    
    def __init__(self):
        """Initialize the logo manager."""
        self._logo_index = {logo.name: logo for logo in self.LOGO_REGISTRY}
        self._category_index = self._build_category_index()
    
    def _build_category_index(self) -> Dict[LogoCategory, List[LogoInfo]]:
        """Build an index of logos by category."""
        index = {category: [] for category in LogoCategory}
        for logo in self.LOGO_REGISTRY:
            index[logo.category].append(logo)
        return index
    
    def get_logo_by_name(self, name: str) -> Optional[LogoInfo]:
        """
        Get a logo by its name.
        
        Args:
            name: The logo name (e.g., 'jk_winners_investment_main')
            
        Returns:
            LogoInfo object if found, None otherwise
        """
        return self._logo_index.get(name)
    
    def get_logos_by_category(self, category: Union[LogoCategory, str]) -> List[LogoInfo]:
        """
        Get all logos in a specific category.
        
        Args:
            category: LogoCategory enum or string ('company', 'division', 'partners', 'investors')
            
        Returns:
            List of LogoInfo objects
        """
        if isinstance(category, str):
            try:
                category = LogoCategory(category.lower())
            except ValueError:
                return []
        
        return self._category_index.get(category, [])
    
    def get_company_logo(self, variant: str = "main") -> Optional[LogoInfo]:
        """
        Get the main company logo.
        
        Args:
            variant: Logo variant ('main' or 'white')
            
        Returns:
            LogoInfo object for the company logo
        """
        name = "jk_winners_investment_main" if variant == "main" else "jk_winners_investment_white"
        return self.get_logo_by_name(name)
    
    def search_logos(self, query: str) -> List[LogoInfo]:
        """
        Search for logos by name or description.
        
        Args:
            query: Search query string
            
        Returns:
            List of matching LogoInfo objects
        """
        query_lower = query.lower()
        results = []
        
        for logo in self.LOGO_REGISTRY:
            if (query_lower in logo.name.lower() or 
                query_lower in logo.description.lower() or
                query_lower in logo.filename.lower()):
                results.append(logo)
        
        return results
    
    def get_all_logos(self) -> List[LogoInfo]:
        """Get all available logos."""
        return self.LOGO_REGISTRY.copy()
    
    def get_logo_url(self, name: str) -> Optional[str]:
        """
        Get the direct URL for a logo.
        
        Args:
            name: Logo name
            
        Returns:
            Direct URL to the logo file
        """
        logo = self.get_logo_by_name(name)
        return logo.url if logo else None
    
    def get_categories(self) -> List[str]:
        """Get all available logo categories."""
        return [category.value for category in LogoCategory]
    
    def to_json(self, pretty: bool = True) -> str:
        """
        Export all logo information as JSON.
        
        Args:
            pretty: Whether to format JSON with indentation
            
        Returns:
            JSON string containing all logo information
        """
        data = {
            "metadata": {
                "version": "1.0.0",
                "repository": "https://github.com/jkwinnersinvestment/JKWI-WEB",
                "base_url": self.BASE_URL,
                "total_logos": len(self.LOGO_REGISTRY),
                "categories": self.get_categories()
            },
            "logos": [logo.to_dict() for logo in self.LOGO_REGISTRY]
        }
        
        if pretty:
            return json.dumps(data, indent=2, ensure_ascii=False)
        return json.dumps(data, ensure_ascii=False)
    
    def generate_html_gallery(self) -> str:
        """
        Generate an HTML gallery of all logos.
        
        Returns:
            HTML string containing a gallery of all logos
        """
        html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JKWI Logo Gallery</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        .header { text-align: center; margin-bottom: 30px; }
        .category { margin-bottom: 40px; }
        .category h2 { color: #333; border-bottom: 2px solid #007acc; padding-bottom: 10px; }
        .logo-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
        .logo-card { background: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .logo-card img { max-width: 100%; height: auto; margin-bottom: 10px; }
        .logo-name { font-weight: bold; color: #333; }
        .logo-description { color: #666; font-size: 14px; margin-top: 5px; }
        .logo-url { font-size: 12px; color: #007acc; word-break: break-all; }
    </style>
</head>
<body>
    <div class="header">
        <h1>JK Winners Investment Logo Gallery</h1>
        <p>Complete collection of JKWI logos organized by category</p>
    </div>
"""
        
        for category in LogoCategory:
            logos = self.get_logos_by_category(category)
            if not logos:
                continue
                
            html += f"""
    <div class="category">
        <h2>{category.value.title()} Logos</h2>
        <div class="logo-grid">
"""
            
            for logo in logos:
                html += f"""
            <div class="logo-card">
                <img src="{logo.url}" alt="{logo.description}" loading="lazy">
                <div class="logo-name">{logo.name}</div>
                <div class="logo-description">{logo.description}</div>
                <div class="logo-url">{logo.url}</div>
            </div>
"""
            
            html += """
        </div>
    </div>
"""
        
        html += """
</body>
</html>
"""
        return html


def main():
    """Main function demonstrating the logo manager usage."""
    # Initialize the logo manager
    manager = JKWILogoManager()
    
    print("=== JKWI Logo Management System ===")
    print(f"Total logos available: {len(manager.get_all_logos())}")
    print(f"Categories: {', '.join(manager.get_categories())}")
    print()
    
    # Example: Get company logo
    company_logo = manager.get_company_logo()
    if company_logo:
        print(f"Main company logo: {company_logo.url}")
    
    # Example: Get all division logos
    division_logos = manager.get_logos_by_category("division")
    print(f"\nDivision logos ({len(division_logos)}):")
    for logo in division_logos:
        print(f"  - {logo.name}: {logo.description}")
    
    # Example: Search for logos
    search_results = manager.search_logos("white")
    print(f"\nWhite variant logos ({len(search_results)}):")
    for logo in search_results[:5]:  # Show first 5
        print(f"  - {logo.name}")
    
    # Export as JSON
    json_data = manager.to_json()
    print(f"\nJSON export ready ({len(json_data)} characters)")


if __name__ == "__main__":
    main()
