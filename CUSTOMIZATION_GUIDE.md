# Customization Guide

This guide will help you quickly customize the service advertisement template for your business.

## Step-by-Step Customization

### 1. Business Information (5 minutes)

Open `index.html` and replace these placeholders:

- **Line 6**: Change `<title>Your Business Name - Professional Services</title>` to your actual business name
- **Line 14**: Replace `<h1>Your Business Name</h1>` in the header
- **Line 28**: Update the hero headline "Professional Services for Your Success"
- **Line 29**: Change the tagline to describe your business
- **Line 152**: Update footer copyright with your business name

### 2. Services Section (10 minutes)

Edit the services in lines 38-61. For each service:

```html
<div class="service-card">
    <div class="icon">🎯</div>  <!-- Change the emoji icon -->
    <h3>Your Service Name</h3>   <!-- Your service title -->
    <p>Your service description</p>  <!-- What you offer -->
</div>
```

**Icon Options**: Use emoji icons like:
- 🎯 Target/Goals
- 💼 Business
- ⚡ Speed/Energy
- 🚀 Growth
- 💡 Ideas
- 🔧 Tools/Tech
- 📊 Analytics
- 🎨 Design
- 📱 Mobile
- 🌐 Web

### 3. Features Section (5 minutes)

Lines 70-91: Update the "Why Choose Us" features with your unique selling points.

### 4. About Section (5 minutes)

Lines 99-106: Write your company story and mission.

Lines 109-125: Update statistics:
- Projects completed
- Happy clients
- Years of experience

### 5. Contact Information (5 minutes)

Lines 134-146: Replace with your actual contact details:
- Email address
- Phone number
- Physical location or service area

### 6. Social Media Links (2 minutes)

Lines 156-158: Add links to your social media profiles.

## Color Customization

Open `styles.css` and modify these color values:

### Primary Colors
- **Line 21**: Header/Footer background: `#2c3e50` (dark blue-gray)
- **Line 53**: Hero gradient start: `#667eea` (purple)
- **Line 53**: Hero gradient end: `#764ba2` (dark purple)
- **Line 68**: Button color: `#3498db` (bright blue)

### To Change the Entire Color Scheme:

1. **Professional Blue**: Use `#2c3e50`, `#3498db`, `#ecf0f1`
2. **Modern Green**: Use `#27ae60`, `#2ecc71`, `#f1f8f4`
3. **Bold Orange**: Use `#e67e22`, `#f39c12`, `#fef5e7`
4. **Elegant Purple**: Use `#8e44ad`, `#9b59b6`, `#f4ecf7`

Search and replace the color codes in `styles.css` to change the entire theme.

## Typography

Current font: System default (San Francisco, Segoe UI, etc.)

To change fonts:
1. Add a Google Font in `index.html` `<head>`:
   ```html
   <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
   ```

2. Update `styles.css` line 7:
   ```css
   font-family: 'Poppins', sans-serif;
   ```

## Adding Your Logo

Replace the text logo in `index.html` (lines 13-15):

```html
<div class="logo">
    <img src="logo.png" alt="Your Business Name" style="height: 40px;">
</div>
```

Then add this to `styles.css`:
```css
.logo img {
    height: 40px;
    width: auto;
}
```

## Making the Contact Form Work

The form currently doesn't submit data. To make it functional:

1. **Using Formspree** (free):
   - Go to https://formspree.io
   - Get your form endpoint
   - Update line 149 in `index.html`:
   ```html
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```

2. **Using Netlify Forms**:
   - Add `netlify` attribute to the form tag
   - Deploy on Netlify

## Quick Tips

- **Images**: Add images by placing them in an `images/` folder and referencing them with `<img src="images/yourimage.jpg">`
- **Videos**: Embed videos in any section using `<iframe>` tags
- **Testimonials**: Add a new section between About and Contact
- **Portfolio**: Add a gallery section with grid layout
- **Pricing**: Create pricing cards similar to service cards

## Testing Your Changes

1. Open `index.html` in a web browser
2. Test all navigation links
3. Resize the browser to test mobile responsiveness
4. Test the form (if you've connected it)
5. Check all sections scroll smoothly

## Need Help?

- HTML basics: https://developer.mozilla.org/en-US/docs/Web/HTML
- CSS basics: https://developer.mozilla.org/en-US/docs/Web/CSS
- Web hosting: GitHub Pages, Netlify, or Vercel (all free)
