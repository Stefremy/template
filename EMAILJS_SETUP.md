 - m# EmailJS Setup Instructions

The contact form in `linke/contato.html` is now configured to send emails to **geral@linke.pt** using EmailJS.

## Setup Steps Required

### 1. Create an EmailJS Account (Free)
- Go to https://www.emailjs.com/
- Sign up for a free account
- Verify your email

### 2. Add Your Email Service
- In EmailJS dashboard, go to **Email Services**
- Click **Add Service**
- Choose **Gmail** (or your email provider)
- Connect your account:
  - For Gmail: Use an [App Password](https://support.google.com/accounts/answer/185833) (recommended for security)
  - Fill in the required fields
- Name the service: `service_linke`
- Click **Create Service**

### 3. Create Email Template
- Go to **Email Templates**
- Click **Create New Template**
- Name it: `template_linke`
- Use this template content:

```
From: {{from_name}} <{{from_email}}>

Informações do Formulário:

Nome: {{from_name}}
Email: {{from_email}}
Telefone: {{phone}}
Empresa: {{company}}

Preço Médio por Envio: {{price_range}}
Soluções Necessárias: {{solutions}}

Mensagem:
{{message}}
```

- Click **Save**

### 4. Copy Your Public Key
- In EmailJS dashboard, go to **Account** > **API Keys**
- Copy your **Public Key**
- Update this line in `linke/contato.html` (line ~1193):
```javascript
emailjs.init("PASTE_YOUR_PUBLIC_KEY_HERE");
```

## Form Configuration

**Current Setup:**
- Service ID: `service_linke`
- Template ID: `template_linke`
- Recipient Email: `geral@linke.pt`

**Form Fields Being Sent:**
- Name
- Email (required)
- Phone
- Company
- Message
- Price Range (Preço médio por envio)
- Solutions Needed (Que solução precisa?)

## Testing

1. Open `linke/contato.html` in a browser
2. Fill out the form
3. Click "Enviar"
4. You should see a success message: "✓ Mensagem enviada com sucesso!"
5. Check `geral@linke.pt` for the email

## Troubleshooting

- **Form not sending?** Check browser console (F12) for errors
- **Email not received?** Verify service ID and template ID match
- **Check EmailJS logs** in your dashboard for delivery status
- **Public Key invalid?** Double-check you're using the correct key

## Notes

- The form is responsive and maintains the original styling
- All form fields are preserved
- Success/error messages appear below the submit button
- Emails include all form data formatted clearly
