# AC Temperature Prediction - Deployment Guide

## ✅ Preparation Complete
Your app is now ready for deployment with:
- `requirements.txt` - all dependencies
- `Procfile` - deployment configuration
- `.gitignore` - exclude unnecessary files
- Updated `app.py` - production mode

## 🚀 Recommended Deployment Platforms

### Option 1: **Render** (Easiest - Free tier available)
1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `gunicorn app:app`
7. Deploy!

### Option 2: **Railway** (Simple - Pay as you go)
1. Go to https://railway.app
2. Sign up
3. Click "New Project" → "Deploy from GitHub"
4. Select your repository
5. Set PORT environment variable if needed
6. Deploy automatically!

### Option 3: **PythonAnywhere** (Python-specific)
1. Go to https://www.pythonanywhere.com
2. Sign up (free tier available)
3. Upload your files via Web
4. Configure WSGI file
5. Reload the app

## 📋 Steps to Deploy (Any Platform)

1. **Initialize Git** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - ready for deployment"
   ```

2. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/your-repo-name.git
   git branch -M main
   git push -u origin main
   ```

3. **Choose your platform above and follow their setup**

## ⚠️ Important Notes

- Your model files (`temperature_model.pkl`, `model_columns.pkl`) are included
- Make sure `100 Samples.xlsx` is in `.gitignore` (already done)
- The free tier may have limitations on file size or execution time
- Always keep sensitive data (API keys, etc.) in environment variables

## 🔍 Troubleshooting

If your app doesn't start:
1. Check the logs on your platform's dashboard
2. Ensure all files are uploaded
3. Verify `.pkl` files are present
4. Check that port binding is correct

## Next Steps
1. Create a GitHub repository
2. Push your code
3. Deploy using one of the platforms above
4. Share your live URL!
