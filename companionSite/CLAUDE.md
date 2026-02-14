# CLAUDE.md - Smart Tangibles Companion Site

## Project Overview

Companion website for **"Smart Tangibles: Strategic Product Management for Connected Hardware"** by Yoel Frischoff.

A living, interactive decision environment that transforms the book from static reading into actionable strategy tools.

## Vision

Establish Smart Tangibles as a continuously updated strategic reference that helps product leaders test ideas, surface platform risk early, and adapt decisions as real-world conditions evolve.

## Target Audience

- Product managers and product leaders building hardware, IoT, smart devices, robotics, mobility, appliances, and medical devices
- Heads of product and fractional CPOs (including senior PMs moving from software into physical products)
- Product-strategy consultants serving hardware companies

## Site Structure

```
/companionSite/
├── index.html              # Main landing page (BUILT)
├── CLAUDE.md               # Project documentation
├── assets/
│   ├── css/style.css      # Main stylesheet (BUILT)
│   ├── js/main.js         # Interactive functionality (BUILT)
│   └── images/            # Site images
├── tools/                  # Interactive calculators/frameworks
│   ├── platform-risk.html
│   ├── defensibility.html
│   ├── cost-asymmetry.html
│   └── validation-checklist.html
├── digest/                 # Weekly digest archive
│   └── archive.html
├── resources/              # Downloadable content
└── chapters/               # Chapter-specific extensions
```

## Key Features (Per Executive Summary)

### 1. Interactive Chapter Extensions
- Hands-on versions of frameworks, diagrams, and checklists
- Connected via QR codes and e-book deep links
- Progressive depth with optional advanced exploration

### 2. Strategic Calculators & Diagnostics
- **Platform Absorption Risk Assessment** - Evaluate feature vulnerability
- **Feature Defensibility Analyzer** - Score across defensibility dimensions
- **Marginal Cost Asymmetry Model** - Compare cost structures vs. software-first competitors
- **Hardware Validation Checklist** - Interactive validation requirements

### 3. Weekly Digest Hub
- Ongoing analysis, signals, case updates
- Searchable archive of prior issues
- Subscriber segmentation by role and industry

### 4. Book Integration
- Sample chapter downloads
- Pre-order functionality
- Chapter-specific companion pages

## Technical Implementation

### Stack
- **Static HTML/CSS/JS** - Fast, simple deployment
- **Google Fonts (Inter)** - Professional typography
- **CSS Variables** - Consistent design tokens
- **Vanilla JavaScript** - No framework dependencies
- **Mobile-first responsive design**

### Design System
```css
--color-primary: #2563eb;      /* Blue */
--color-bg-dark: #0f172a;      /* Dark navy */
--font-family: 'Inter';
--border-radius: 8px;
```

### Current Status
- **index.html** - Complete landing page with all sections
- **style.css** - Full responsive stylesheet
- **main.js** - Mobile nav, form handling, scroll animations
- **Directory structure** - Created and ready

## Next Development Steps

1. **Tools Pages** - Build interactive calculator interfaces
2. **Digest System** - Email capture integration (ConvertKit/Buttondown)
3. **Chapter Extensions** - Individual companion pages
4. **Analytics** - Tracking for engagement metrics
5. **Book Cover** - Replace placeholder with actual cover image

## Business Model Context

Value amplifier for the book that converts engagement into higher-value offerings:
- Free/lightly gated tools and digest
- Paid subscription for advanced diagnostics
- Services funnel: keynotes, workshops, strategic advisory

## Contact

**Author**: Yoel Frischoff
**Consultancy**: TheRoad
**Email**: yoel@theroad.co.il
**Book**: Smart Tangibles (2025/2026)
