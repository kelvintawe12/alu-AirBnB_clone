# AirBnB Clone - Web Static

This repository contains the web static files for the AirBnB Clone project. The goal of this project is to create a front-end for the AirBnB Clone website, focusing on structuring HTML and CSS files for various components of the site.

## Table of Contents

1. [Project Description](#project-description)
2. [File Structure](#file-structure)
3. [Usage](#usage)
4. [HTML Files](#html-files)
5. [CSS Files](#css-files)
6. [Images](#images)
7. [Getting Started](#getting-started)
8. [Authors](#authors)

## Project Description

The AirBnB Clone project is a web-based clone of the AirBnB platform. It involves creating static web pages with headers, footers, filters, and places listings using HTML and CSS. The project is organized into multiple iterations, each adding features to the static design.

## File Structure

The project follows a structured layout:

```
web_static/
├── images/
│   ├── favicon.ico
│   ├── logo.png
├── styles/
│   ├── 3-common.css
│   ├── 3-header.css
│   ├── 3-footer.css
│   ├── 4-filters.css
│   ├── 5-filters.css
│   ├── 6-filters.css
│   ├── 7-places.css
├── 3-index.html
├── 4-index.html
├── 5-index.html
├── 6-index.html
├── 7-index.html
```

## Usage

Open any of the `.html` files in a web browser to view the static pages. Each file represents a different iteration of the project with additional features.

## HTML Files

### `3-index.html`
- Displays a header and footer.
- Includes the basic structure of the website with placeholders for content.

### `4-index.html`
- Adds a filters section to the page.
- Includes a search button with styled properties.

### `5-index.html`
- Adds filters for "Locations" and "Amenities."
- Displays headers and subheaders inside the filters.

### `6-index.html`
- Updates filters to display a contextual dropdown menu on hover.
- Location filter supports a nested structure (state -> cities).

### `7-index.html`
- Adds a "Places" section to display search results.
- Each "Place" is an article with styled content.

## CSS Files

### `3-common.css`
- Global styles for body and container elements.
- Font settings: color, size, and family.

### `3-header.css`
- Styles for the header section:
    - Background color: white.
    - Border-bottom: 1px solid #CCCCCC.
    - Includes logo styling as a background image.

### `3-footer.css`
- Styles for the footer section:
    - Background color: white.
    - Border-top: 1px solid #CCCCCC.
    - Text is vertically and horizontally centered.

### `4-filters.css`
- Styles for the filters section:
    - Adds a search button with hover effects.
    - Filters box with white background and borders.

### `5-filters.css`
- Adds styles for the "Locations" and "Amenities" filters:
    - Styled headers and subheaders.
    - Borders between filter sections.

### `6-filters.css`
- Adds styles for dropdown menus:
    - Dropdowns styled as `.popover` with a light background and borders.
    - Nested structure for the "Locations" filter.

### `7-places.css`
- Adds styles for the "Places" section:
    - Articles for each place with borders, padding, and margins.
    - Place name styled in the center of the article.

## Images

- `favicon.ico`: Icon displayed in the browser tab.
- `logo.png`: Background image for the logo in the header.

## Getting Started

To view the project:
1. Clone the repository.
     ```bash
     git clone https://github.com/alu-AirBnB_clone.git
     ```
2. Navigate to the `web_static` directory.
3. Open any `.html` file in your browser to view the corresponding page.

## Authors

- **Your Name**
- Inspired by the ALU AirBnB Clone project.

---

Feel free to reach out for suggestions or contributions!