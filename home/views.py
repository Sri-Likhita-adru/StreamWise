from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
import os
import matplotlib.pyplot as plt
import io
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

from django.core.files.storage import FileSystemStorage
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from keras.models import load_model
from .models import AnalysisResult
from .models import TelegramAnalysis
from ultralytics import YOLO
from IPython import display
display.clear_output()
import ultralytics
from transformers import BertTokenizer
flagged_keywords = ["baby Dogecoin", "doge meme token", "ran up", "Shiba Inu", "ranked 176", "mid cap", "Doge will go to one dollar", "next Bull Run", "chance to run at least like 10x", "older tokens", "crypto gaming tokens", "50 2000 acts in the next Bull Run", "earning passive rewards", "web 3 gaming node owner", "earning 25 every day without doing anything", "opportunity is huge", "baby doll Shogun", "20x is doable", "risk reward", "buying crypto gaming tokens", "crypto will not be broken", "bypassed", "ground shattering", "digital currency", "profitable", "Bitcoin Sheba and ethereum", "truer words", "highly profitable", "Sensational cryptocurrencies", "millionaire", "huge fluctuations", "volatile", "evolving constantly", "opportunities and drawbacks", "positive and negative aspects", "trend in the broader cryptocurrency Market", "positive developments", "promising year", "pessimistic scenario", "top five mobile cryptocurrency earning apps for ios", "make money with NFTs", "buy for $20 and then sell a week later for like $2000", "minted or got the NFT for $250, and eleven days later, he sold it for $1200", "huge profit", "quick profit", "blow up to become highly profitable", "minting an NFT and selling it right away", "whitelisted people can mint an NFT", "public minting period", "Tron Wars", "Awesome Apes", "normal people", "influencer NFTs", "Logan Paul", "Paris Hilton", "Gary Vee", "Avenged Sevenfold", "experience", "goals", "reputation", "good or bad reputation", "student who sold his selfies as NFTs", "time-lapse college projects", "trustworthy founders", "investing in the right NFT project", "believe in", "long term investments", "make a big profit", "investing in things that I believe in", "analyze NFT projects", "invest in the right NFT project", "guaranteed profits", "surefire method", "foolproof strategy", "never fail", "100% success rate", "risk-free", "unlimited gains", "secret formula", "exclusive insider information", "market manipulation", "manipulate prices", "insider tips", "unbeatable strategy", "confidential details", "hidden patterns", "never-before-seen method", "automatic profits", "set it and forget it", "magic software", "algorithmic trading", "profit-pulling machine", "money-making software", "autopilot earnings", "secret trading technique", "surefire signals", "never lose", "no-risk strategy", "exclusive formula", "guaranteed success", "foolproof method", "hidden strategies", "profit of 345", "easily get 200", "good special profit", "bonus of $100", "Protective Prot", "IC is a protector", "50% deposit bonus", "magic software", "automatic profits", "unlimited gains", "exclusive insider information", "manipulate prices", "insider tips", "unbeatable strategy", "hidden patterns", "set it and forget it", "money-making software", "autopilot earnings", "surefire signals", "no-risk strategy", "exclusive formula", "guaranteed success", "foolproof method", "hidden strategies", "profit of 13 $9", "join the Telegram channel for this setting", "very good profit", "profit is made here", "unique strategy", "live proof", "95% results", "follow the strategy", "follow on Instagram", "expert option", "create an account", "promo code", "50% opposite bonus", "make $200", "bonus of $1", "get $300", "link in the description", "subscribe to the channel", "follow on Instagram", "exclusive insights", "secret technique", "hidden knowledge", "guaranteed profits", "insider advantage", "proprietary formula", "exclusive access", "guaranteed crypto profits", "instant crypto gains", "exclusive crypto strategy", "secret crypto method", "quick crypto riches", "massive crypto returns", "surefire crypto investment", "insider crypto tips", "risk-free crypto trading", "sky-high crypto growth", "overnight crypto success", "hidden crypto opportunity", "next big crypto winner", "explosive crypto growth", "unbeatable crypto results", "never-fail crypto system", "100% crypto success rate", "proven crypto formula", "zero-risk crypto profit", "foolproof crypto plan", "limited-time crypto offer", "can't lose crypto trade", "guaranteed crypto success", "game-changing crypto strategy", "crypto millionaire maker", "unlock the crypto secret", "rare crypto opportunity", "guaranteed crypto breakthrough", "predict crypto market trends", "exclusive crypto insights", "revolutionary crypto method", "predict the future of crypto", "unlimited crypto potential", "bulletproof crypto strategy", "guaranteed crypto riches", "top-secret crypto technique", "golden ticket crypto investment", "guaranteed crypto victory", "future-proof crypto gains", "ultimate crypto profit formula", "exclusive crypto trading secrets", "guaranteed crypto performance", "instant crypto success", "exclusive crypto profit opportunity", "hidden crypto advantage", "crypto profit explosion", "risk-free crypto gains", "unstoppable crypto growth", "massive crypto profits", "time-tested crypto strategy", "crypto insider knowledge", "foolproof crypto approach", "proven crypto success", "zero-loss crypto formula", "can't-miss crypto opportunity", "guaranteed crypto results", "revolutionize your crypto finances", "never-fail crypto approach", "exponential crypto gains", "undiscovered crypto gem", "guaranteed crypto returns", "secret crypto formula", "exclusive crypto profit formula", "foolproof crypto method", "unbeatable crypto gains", "life-changing crypto opportunity", "limited-time crypto deal", "can't-fail crypto strategy", "guaranteed crypto wealth", "game-changing crypto solution", "next big crypto breakout", "unprecedented crypto growth", "predictive crypto power", "exclusive crypto secret", "guaranteed crypto breakthrough", "unlimited crypto success", "golden crypto opportunity", "guaranteed crypto prosperity", "future-proof crypto strategy", "instant crypto profits", "exclusive crypto formula", "proven crypto techniques", "risk-free crypto profits", "massive crypto success", "hidden crypto secrets", "ultimate crypto profit potential", "fail-proof crypto method", "unstoppable crypto returns", "crypto insider methods", "guaranteed crypto advantage", "exclusive crypto insights", "exponential crypto growth", "zero-risk crypto gains", "unbeatable crypto success", "life-changing crypto results", "never-before-revealed crypto strategy", "revolutionary crypto approach", "predict crypto market movements", "undiscovered crypto opportunity", "guaranteed crypto strategy", "future-proof crypto profit", "top-secret crypto method", "guaranteed crypto victory", "game-changing crypto method", "surefire crypto profit", "exclusive crypto profit secrets", "hidden crypto potential", "risk-free crypto strategy", "unstoppable crypto profit", "massive crypto returns", "time-tested crypto techniques", "crypto insider secrets", "foolproof crypto solution", "proven crypto approaches", "zero-loss crypto strategy", "can't-miss crypto chance", "guaranteed crypto returns", "revolutionize your crypto success", "never-fail crypto solution", "exponential crypto profits", "undiscovered crypto treasure", "guaranteed crypto breakthrough", "guaranteed returns", "instant profits", "secret method", "exclusive offer", "quick gains", "massive returns", "surefire strategy", "insider tips", "risk-free investment", "sky-high growth", "overnight success", "hidden opportunity", "next big winner", "explosive growth", "unbeatable results", "never-fail system", "100% success rate", "proven formula", "zero-risk profit", "foolproof plan", "life-changing earnings", "limited-time offer", "can't lose", "guaranteed success", "game-changing strategy", "millionaire maker", "unlock the secret", "rare opportunity", "guaranteed breakthrough", "predict the future", "exclusive access", "never-before-seen", "revolutionary method", "predict market trends", "unlimited potential", "bulletproof strategy", "guaranteed riches", "top-secret technique", "golden ticket", "guaranteed victory", "future-proof investment", "zero effort, maximum gains", "ultimate profit formula", "exclusive insights", "guaranteed wealth", "fail-proof system", "next big thing", "surefire winner", "insider trading secrets", "guaranteed performance", "instant success", "exclusive profit method", "hidden advantage", "profit explosion", "risk-free gains", "unstoppable growth", "massive profits", "time-tested strategy", "insider knowledge", "foolproof approach", "proven success", "zero-loss formula", "can't-miss opportunity", "guaranteed results", "revolutionize your finances", "never-fail approach", "exponential gains", "undiscovered gem", "guaranteed returns", "secret formula", "exclusive profit opportunity", "foolproof method", "unbeatable gains", "life-changing opportunity", "limited-time deal", "can't-fail strategy", "guaranteed wealth", "game-changing solution", "next big breakout", "unprecedented growth", "predictive power", "exclusive secret", "guaranteed breakthrough", "unlimited success", "golden opportunity", "guaranteed prosperity", "future-proof strategy", "instant profits", "exclusive formula", "proven techniques", "risk-free profits", "massive success", "hidden secrets", "ultimate profit potential", "fail-proof method", "unstoppable returns", "insider methods", "guaranteed advantage", "exclusive insights", "exponential growth", "zero-risk gains", "unbeatable success", "life-changing results", "never-before-revealed strategy", "revolutionary approach", "predict market movements", "undiscovered opportunity", "guaranteed strategy", "future-proof profit", "top-secret method", "guaranteed victory", "game-changing method", "surefire profit", "exclusive profit secrets", "hidden potential", "risk-free strategy", "unstoppable profit", "massive returns", "time-tested techniques", "insider secrets", "foolproof solution", "proven approaches", "zero-loss strategy", "can't-miss chance", "guaranteed returns", "revolutionize your success", "never-fail solution", "exponential profits", "undiscovered treasure", "guaranteed breakthrough", "next Dogecoin", "guaranteed meme coin gains", "instant meme coin profits", "exclusive meme coin strategy", "secret meme coin method", "quick meme coin riches", "massive meme coin returns", "surefire meme coin investment", "insider meme coin tips", "sky-high meme coin growth", "overnight meme coin success", "hidden meme coin opportunity", "next big meme coin winner", "explosive meme coin growth", "unbeatable meme coin results", "never-fail meme coin system", "100% meme coin success rate", "proven meme coin formula", "zero-risk meme coin profit", "foolproof meme coin plan", "limited-time meme coin offer", "can't lose meme coin trade", "guaranteed meme coin success", "game-changing meme coin strategy", "meme coin millionaire maker", "unlock the meme coin secret", "rare meme coin opportunity", "guaranteed meme coin breakthrough", "predict meme coin trends", "exclusive meme coin insights", "revolutionary meme coin method", "predict the future of meme coins", "unlimited meme coin potential", "bulletproof meme coin strategy", "guaranteed meme coin riches", "top-secret meme coin technique", "golden ticket meme coin investment", "guaranteed meme coin victory", "future-proof meme coin gains", "ultimate meme coin profit formula", "exclusive meme coin trading secrets", "guaranteed meme coin performance", "instant meme coin success", "exclusive meme coin profit opportunity", "hidden meme coin advantage", "meme coin profit explosion", "risk-free meme coin gains", "unstoppable meme coin growth", "massive meme coin profits", "time-tested meme coin strategy", "meme coin insider knowledge", "foolproof meme coin approach", "proven meme coin success", "zero-loss meme coin formula", "can't-miss meme coin opportunity", "guaranteed meme coin results", "revolutionize your meme coin finances", "never-fail meme coin approach", "exponential meme coin gains", "undiscovered meme coin gem", "guaranteed meme coin returns", "secret meme coin formula", "exclusive meme coin profit formula", "foolproof meme coin method", "unbeatable meme coin gains", "life-changing meme coin opportunity", "limited-time meme coin deal", "can't-fail meme coin strategy", "guaranteed meme coin wealth", "game-changing meme coin solution", "next big meme coin breakout", "unprecedented meme coin growth", "predictive meme coin power", "exclusive meme coin secret", "guaranteed meme coin breakthrough", "unlimited meme coin success", "golden meme coin opportunity", "guaranteed meme coin prosperity", "future-proof meme coin strategy", "instant meme coin profits", "exclusive meme coin formula", "proven meme coin techniques", "risk-free meme coin profits", "massive meme coin success", "hidden meme coin secrets", "ultimate meme coin profit potential", "fail-proof meme coin method", "unstoppable meme coin returns", "meme coin insider methods", "guaranteed meme coin advantage", "exclusive meme coin insights", "exponential meme coin growth", "zero-risk meme coin gains", "unbeatable meme coin success", "life-changing meme coin results", "never-before-revealed meme coin strategy", "revolutionary meme coin approach", "predict meme coin market movements", "undiscovered meme coin opportunity", "guaranteed meme coin strategy", "future-proof meme coin profit", "top-secret meme coin method", "guaranteed meme coin victory", "game-changing meme coin method", "surefire meme coin profit", "exclusive meme coin profit secrets", "hidden meme coin potential", "risk-free meme coin strategy", "unstoppable meme coin profit", "massive meme coin returns", "time-tested meme coin techniques", "meme coin insider secrets", "foolproof meme coin solution", "proven meme coin approaches", "zero-loss meme coin strategy", "can't-miss meme coin chance", "guaranteed meme coin returns", "revolutionize your meme coin success", "never-fail meme coin solution", "exponential meme coin profits", "undiscovered meme coin treasure", "guaranteed meme coin breakthrough"]
sebi_registered_apps = ["Zerodha Broking Limited", "Angel Broking Limited", "5PAISA Capital Limited", "ICICI Securities Limited", "Motilal Oswal Financial Services Limited", "Sharekhan Limited", "Kotak Securities Limited", "HDFC Securities Limited", "IIFL Securities Limited", "Edelweiss Broking Limited", "Axis Securities Limited", "Tradebulls Securities (P) Limited", "Dhani Stocks Limited", "SMC Global Securities Limited", "Religare Broking Limited", "IDBI Capital Markets & Securities Limited", "Reliance Securities Limited", "SBICAP Securities Limited", "Karvy Stock Broking Limited", "Anugrah Stock & Broking Private Limited", "Indianivesh Shares and Securities Private Limited", "RKSV Securities India Private Limited", "Arcadia Share & Stock Brokers Private Limited", "Alice Blue Financial Services Limited", "Fyers Securities Private Limited", "Action Financial Services (India) Limited", "Modex International Securities Limited", "Aditya Birla Money Limited", "Samco Securities Limited", "Geojit Financial Services Limited", "Astha Credit & Securities (P) Limited", "Profitmart Securities Private Limited", "Conard Securities Private Limited", "Sumpoorna Portfolio Limited", "Vikson Securities Private Limited", "Nirmal Bang Securities Private Limited", "Ventura Securities Limited", "Anand Rathi Share and Stock Brokers Limited", "BMA Wealth Creators Limited", "Finvasia Securities Private Limited", "Dealmoney Securities Private Limited", "Globe Capital Market Limited", "SMIFS Limited", "Swastika Investmart Limited", "Goodwill Wealth Management Private Limited", "YES Securities (India) Limited", "Nextbillion Technology Private Limited", "Navia Markets Limited", "Choice Equity Broking Private Limited", "Yuvraj Securities", "SHCIL Services Limited", "Zerodha Securities Private Limited", "Integrated Enterprises (India) Private Limited", "Astitva Capital Market Private Limited", "Monarch Networth Capital Limited", "Shri Parasram Holdings Private Limited", "Quantum Global Securities Limited", "Master Capital Services Limited", "Reflection Investments", "LKP Securities Limited", "Prabhudas Lilladher Private Limited", "VNS Finance & Capital Services Limited", "Shriram Insight Share Brokers Limited", "Bonanza Portfolio Limited", "Motilal Oswal Capital Markets Private Limited", "JM Financial Services Limited", "Karmic Stock Broking Private Limited", "Zebu Share and Wealth Managements Private Limited", "Alankit Imaginations Limited", "Stock Holding Corporation of India Limited", "Prudent Broking Services Private Limited", "South Asian Stocks Limited", "Maxgrowth Capital Private Limited", "Ashlar Securities Private Limited", "Acumen Capital Market (India) Limited", "NJ Invest India Private Limited", "HEM Finlease Private Limited", "BOB Capital Markets Limited", "Arihant Capital Markets Limited", "Abhipra Capital Limited", "Fairwealth Securities Limited", "Mehta Equities Limited", "LFS Broking Private Limited", "Century Finvest Private Limited", "ISS Enterprise Limited", "Marwadi Shares and Finance Limited", "Elite Wealth Advisors Limited", "Raghunandan Capital Private Limited", "Escorts Securities Limited", "Comfort Securities Limited", "Paytm Money Limited", "Mandot Securities Private Limited", "IFCI Financial Services Limited", "ICICI Web Trade Limited", "Nine Star Broking Private Limited", "Latin Manharlal Securities Private Limited", "Wealth India Financial Services Limited", "Lohia Securities Limited", "Adwealth Stock Broking Private Limited", "Mansukh Securities and Finance Limited", "Aum Capital Market Private Limited", "Anush Shares and Securities Private Limited", "Pune E Stock Broking Private Limited", "Badjate Stock and Shares Private Limited", "KR Choksey Shares and Securities Private Limited", "Findoc Investmart Private Limited", "Karuna Financial Services Private Limited", "Zuari Finserv Limited", "GCL Securities Private Limited", "Sunlight Broking LLP", "CD Equisearch Private Limited", "Aasma Securities Private Limited", "Kotak Mahindra Bank Limited", "Wealthstreet Advisors Private Limited", "Kedia Shares and Stocks Brokers Limited", "NKB Securities", "Ambalal Shares and Stocks Private Limited", "Signature Global Securities Private Limited", "Prognosis Securities Private Limited", "Garg Securities Private Limited", "CIL Securities Limited", "Coimbatore Capital Limited", "Aditya Ajay Share Brokers Private Limited", "OJ Financial Services Limited", "DP Tradeking Private Limited", "Dynamic Equities Private Limited", "Farsight Securities Limited", "ISF Securities Limited", "R Wadiwala Securities Private Limited", "Enrich Financial Solution Private Limited", "Multiplex Capital Limited", "Progressive Share Brokers Private Limited", "Shilpa Stock Broker Private Limited", "Nirmal Bang Equities Private Limited", "Fair Intermediate Investments Private Limited", "AS Stock Broking and Management Private Limited", "Patel Wealth Advisors Private Limited", "Stampede Capital Limited", "Pravin Ratilal Share and Stock Brokers Limited", "Crown Consultants Private Limited", "Abhira Securities Limited", "Mittal Securities Private Limited", "Jhaveri Securities Limited", "Sara Securities Private Limited", "Jyoti Portfolio Private Limited", "Rudra Shares and Stock Brokers Limited", "KK Securities Limited", "BN Rathi Securities Limited", "Khandwala Securities Limited", "Rajsons Securities Limited"]
sebi_alert_apps=[]
# Initialize the tokenizer once
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")




    




def index(request):
  context = {
    'segment': 'index'
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/tables.html", context)

# Components
@login_required(login_url='/accounts/login/')
def bc_button(request):
  context = {
    'parent': 'basic_components',
    'segment': 'button'
  }
  return render(request, "pages/components/bc_button.html", context)

@login_required(login_url='/accounts/login/')
def bc_badges(request):
  context = {
    'parent': 'basic_components',
    'segment': 'badges'
  }
  return render(request, "pages/components/bc_badges.html", context)

@login_required(login_url='/accounts/login/')
def bc_breadcrumb_pagination(request):
  context = {
    'parent': 'basic_components',
    'segment': 'breadcrumbs_&_pagination'
  }
  return render(request, "pages/components/bc_breadcrumb-pagination.html", context)

@login_required(login_url='/accounts/login/')
def bc_collapse(request):
  context = {
    'parent': 'basic_components',
    'segment': 'collapse'
  }
  return render(request, "pages/components/bc_collapse.html", context)

@login_required(login_url='/accounts/login/')
def bc_tabs(request):
  context = {
    'parent': 'basic_components',
    'segment': 'navs_&_tabs'
  }
  return render(request, "pages/components/bc_tabs.html", context)

@login_required(login_url='/accounts/login/')
def bc_typography(request):
  context = {
    'parent': 'basic_components',
    'segment': 'typography'
  }
  return render(request, "pages/components/bc_typography.html", context)

@login_required(login_url='/accounts/login/')
def icon_feather(request):
  context = {
    'parent': 'basic_components',
    'segment': 'feather_icon'
  }
  return render(request, "pages/components/icon-feather.html", context)


# Forms and Tables
@login_required(login_url='/accounts/login/')
def form_elements(request):
  context = {
    'parent': 'form_components',
    'segment': 'form_elements'
  }
  return render(request, 'pages/form_elements.html', context)

@login_required(login_url='/accounts/login/')
def basic_tables(request):
  context = {
    'parent': 'tables',
    'segment': 'basic_tables'
  }
  return render(request, 'pages/tbl_bootstrap.html', context)

# Chart and Maps
@login_required(login_url='/accounts/login/')
def morris_chart(request):
  context = {
    'parent': 'chart',
    'segment': 'morris_chart'
  }
  return render(request, 'pages/chart-morris.html', context)

@login_required(login_url='/accounts/login/')
def google_maps(request):
  context = {
    'parent': 'maps',
    'segment': 'google_maps'
  }
  return render(request, 'pages/map-google.html', context)

# Authentication
class UserRegistrationView(CreateView):
  template_name = 'accounts/auth-signup.html'
  form_class = RegistrationForm
  success_url = '/accounts/login/'

class UserLoginView(LoginView):
  template_name = 'accounts/auth-signin.html'
  form_class = LoginForm

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/auth-reset-password.html'
  form_class = UserPasswordResetForm

class UserPasswrodResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/auth-password-reset-confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/auth-change-password.html'
  form_class = UserPasswordChangeForm

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

@login_required(login_url='/accounts/login/')
def profile(request):
  context = {
    'segment': 'profile',
  }
  return render(request, 'pages/profile.html', context)

@login_required(login_url='/accounts/login/')
def sample_page(request):
  context = {
    'segment': 'sample_page',
  }
  return render(request, 'pages/sample-page.html', context)

@login_required(login_url='/accounts/login/')
def profile(request):
    misleading_results = AnalysisResult.objects.filter(conclusion='misleading')
    return render(request, 'pages/profile.html', {'misleading_results': misleading_results})



@login_required(login_url='/accounts/login/')
def telegram(request):
    c=AnalysisResult.objects.count()
    last_uploaded_text = None
    
    if request.method == 'POST':
      name=request.POST.get('name')
      age=request.POST.get('age')
      school=request.POST.get('school')
      sub = request.POST.get('favorite_subjects')
      tech = request.POST.get('technology_likes')
      project = request.POST.get('projects_done')
      hobby = request.POST.get('hobbies')
      goals = request.POST.get('goal')
      desc1=sub+tech+project+hobby+goals
      print(desc1)

      import openai

      # Set your OpenAI GPT-3 API key
      api_key = ""
      

      # Description for which you want an explanation
      prompt="I am giving you the response of a 10th grade student regarding his favourite subject, technology he likes, projects he has done, his hobbies and his goal in his life. Summarise it in 100 words"+"/n"+desc1
      # Generate explanation using GPT-3 API
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=150,
          stop=None,
          temperature=0.7
      )

      explanation = response.choices[0].text.strip()
      print(explanation) 

      

      #-------------------------------------------------------------------------------------------------------------
      #PERSONALITY REPORT
      questionnaire_answers_json = request.POST.get('questionnaire_answers')
      qa= json.loads(questionnaire_answers_json)
      print(qa) 
      questions = [
            "I enjoy solving complex puzzles and problems.",
            "I am comfortable working in a team and collaborating with others.",
            "I prefer working independently rather than in a group.",
            "I am open to trying new technologies and learning new skills.",
            "I am detail-oriented and pay close attention to accuracy.",
            "I enjoy programming and coding tasks.",
            "I find satisfaction in helping others with their technical problems.",
            "I prefer a structured and organized approach to my work.",
            "I enjoy taking on leadership roles in group projects.",
            "I am comfortable with ambiguity and uncertainty.",
            "I value work-life balance and prioritize it in my life.",
            "I enjoy experimenting with new ideas and solutions.",
            "I am patient and persistent when faced with challenges.",
            "I am interested in ethical considerations in technology and its impact on society.",
            "I enjoy presenting my ideas and findings to others.",
            "I am skilled at time management and meeting deadlines.",
            "I have a strong desire to innovate and create new solutions.",
            "I am comfortable with a fast-paced and dynamic work environment.",
            "I am interested in exploring the intersection of technology and other fields (e.g., healthcare, finance).",
            "I am motivated to continuously update my technical knowledge and skills.",
            "I enjoy mentoring and helping others learn technical concepts.",
            "I find it easy to adapt to new software tools and technologies.",
            "I am comfortable giving and receiving constructive feedback.",
            "I prefer working on long-term projects rather than short-term tasks.",
            "I enjoy exploring and experimenting with emerging technologies.",
            "I can handle high-pressure situations effectively.",
            "I believe in the importance of diversity and inclusion in the tech industry.",
            "I am interested in exploring entrepreneurial opportunities in technology.",
            "I am proactive in seeking solutions to technical challenges.",
            "I am passionate about using technology for social impact and positive change."
            ]
      q_str=""
      for i in range(len(qa)):
        q_str=q_str+str(questions[i])+":"
        q_str=q_str+str(qa[i])+"/n"
      
      prompt="I have conducted a 10th grade student a personality test with a questionnaire of 30 questions with options Strongly Disagree,Disagree,Neutral,Agree, Strongly Agree. Now I am giving all the questions and the corresponding answer given by the student. Genrate me a report about his personality regarding in the topics such as extraversion, Conscientiousness, agreeableness, openness to experience, emotional stability, polychronicity. I need somewhat detailed report."+"/n"+q_str
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=500,
          stop=None,
          temperature=0.7
      )

      personality = response.choices[0].text.strip()
      print(personality) 






      #------------------------------------------------------------------------------------------------------------
      import pickle
      import pandas as pd
      df=pd.read_csv('home\stream.csv')
      namee = df["Name"]
      namee = namee.str.rstrip('.txt')
      namee
      model = pickle.load(open('home\BM25_Model(2).sav', 'rb'))
      query_array = explanation+personality
      recome=model.get_top_n(query_array.split(" "), namee, n=5)
      recom=""
      for i in recome:
        recom=recom+str(i)
      #recom="B-Tech Artificial Intelligence and Data Science, BE Computer Science and Engineering, B-Tech Robotics Engineering, B-Tech Computer Science and Business Systems,B-Tech Information Technology"



 
      #Overall report
      #------------------------------------------------------------------------------------------------------------
      prompt="We are recommending suitable course to take in 11thstd for a 10th grade student. we got some inputs from the student regarding his interest, hobbies, projects etc and we have also conducted a personality test using a questionnaire containing 30 questions. Now we have report about his interest, peronality report based on questionnaire. Our bm25 model have given 5 course recommendations based on the reports. now you have to give the overall report based on the general report, personality report and the recommendation given by our model. Tell how the recommendation will suite him and you have to justify it"+"/n"+"General report"+"/n"+explanation+"/n"+"Personality report"+"/n"+personality+"/n"+"Recommendations"+recom
      # Generate explanation using GPT-3 API
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=150,
          stop=None,
          temperature=0.7
      )

      overall = response.choices[0].text.strip()
      print(overall) 

      analysis = TelegramAnalysis(
            name=name,
            age=age,
            school=school,
            subjects=sub,
            Technology=tech,
            projects=project,
            hobby=hobby,
            goal=goals,
            questionnaire_summary=q_str,
            recommendations=recom,
            general_report=explanation,
            personality_report=personality,
            overall_report=overall
            
      )
      analysis.save()  
      return redirect('result')

    return render(request, 'pages/telegram.html',  {'latest_analysis_result': last_uploaded_text})
   
import json
@login_required(login_url='/accounts/login/')
def youtube(request):
    c=AnalysisResult.objects.count()
    last_uploaded_text = None
    
    if request.method == 'POST':
      name=request.POST.get('name')
      age=request.POST.get('age')
      school=request.POST.get('school')
      sub = request.POST.get('favorite_subjects')
      tech = request.POST.get('technology_likes')
      project = request.POST.get('projects_done')
      hobby = request.POST.get('hobbies')
      goals = request.POST.get('goal')
      desc1=sub+tech+project+hobby+goals
      print(desc1)

      import openai

      # Set your OpenAI GPT-3 API key
      api_key = ""
      

      # Description for which you want an explanation
      prompt="I am giving you the response of a 12th grade student regarding his favourite subject, technology he likes, projects he has done, his hobbies and his goal in his life. Summarise it in 100 words"+"/n"+desc1
      # Generate explanation using GPT-3 API
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=150,
          stop=None,
          temperature=0.7
      )

      explanation = response.choices[0].text.strip()
      print(explanation) 

      

      #-------------------------------------------------------------------------------------------------------------
      #PERSONALITY REPORT
      questionnaire_answers_json = request.POST.get('questionnaire_answers')
      qa= json.loads(questionnaire_answers_json)
      print(qa) 
      questions = [
            "I enjoy solving complex puzzles and problems.",
            "I am comfortable working in a team and collaborating with others.",
            "I prefer working independently rather than in a group.",
            "I am open to trying new technologies and learning new skills.",
            "I am detail-oriented and pay close attention to accuracy.",
            "I enjoy programming and coding tasks.",
            "I find satisfaction in helping others with their technical problems.",
            "I prefer a structured and organized approach to my work.",
            "I enjoy taking on leadership roles in group projects.",
            "I am comfortable with ambiguity and uncertainty.",
            "I value work-life balance and prioritize it in my life.",
            "I enjoy experimenting with new ideas and solutions.",
            "I am patient and persistent when faced with challenges.",
            "I am interested in ethical considerations in technology and its impact on society.",
            "I enjoy presenting my ideas and findings to others.",
            "I am skilled at time management and meeting deadlines.",
            "I have a strong desire to innovate and create new solutions.",
            "I am comfortable with a fast-paced and dynamic work environment.",
            "I am interested in exploring the intersection of technology and other fields (e.g., healthcare, finance).",
            "I am motivated to continuously update my technical knowledge and skills.",
            "I enjoy mentoring and helping others learn technical concepts.",
            "I find it easy to adapt to new software tools and technologies.",
            "I am comfortable giving and receiving constructive feedback.",
            "I prefer working on long-term projects rather than short-term tasks.",
            "I enjoy exploring and experimenting with emerging technologies.",
            "I can handle high-pressure situations effectively.",
            "I believe in the importance of diversity and inclusion in the tech industry.",
            "I am interested in exploring entrepreneurial opportunities in technology.",
            "I am proactive in seeking solutions to technical challenges.",
            "I am passionate about using technology for social impact and positive change."
            ]
      q_str=""
      for i in range(len(qa)):
        q_str=q_str+str(questions[i])+":"
        q_str=q_str+str(qa[i])+"/n"
      
      prompt="I have conducted a 12th grade student a personality test with a questionnaire of 30 questions with options Strongly Disagree,Disagree,Neutral,Agree, Strongly Agree. Now I amgiving all the questions and the corresponding answer given by the student. Genrate me a report about his personality regarding in the topics such as extraversion, Conscientiousness, agreeableness, openness to experience, emotional stability, polychronicity. I need somewhat detailed report."+"/n"+q_str
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=500,
          stop=None,
          temperature=0.7
      )

      personality = response.choices[0].text.strip()
      print(personality) 





      #Recommendation
      #------------------------------------------------------------------------------------------------------------
      import pickle
      import pandas as pd
      df=pd.read_csv('home\output.csv')
      namee = df["Name"]
      namee = namee.str.rstrip('.txt')
      namee
      model = pickle.load(open('home\BM25_Model.sav', 'rb'))
      query_array = explanation+personality
      recome=model.get_top_n(query_array.split(" "), namee, n=5)
      recom=""
      for i in range(len(recome)):
        if i==len(recome)-1:
          recom=recom[i]+str(i)
        else:  
          recom=recom[i]+str(i)+" , "



 
      #Overall report
      #------------------------------------------------------------------------------------------------------------
      prompt="We are recommending suitable course to take in college for a 12th grade student. we got some inputs from the student regarding his interest, hobbies, projects etc and we have also conducted a personality test using a questionnaire containing 30 questions. Now we have reort about his interest, peronality report based on questionnaire. Our bm25 model have given 5 course recommendations based on the reports. now you have to give the overall report based on the general report, personality report and the recommendation given by our model. Tell how the recommendation will suite him and you have to justify it"+"/n"+"General report"+"/n"+explanation+"/n"+"Personality report"+"/n"+personality+"/n"+"Recommendations"+recom
      # Generate explanation using GPT-3 API
      openai.api_key = api_key
      response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=150,
          stop=None,
          temperature=0.7
      )

      overall = response.choices[0].text.strip()
      print(overall) 

      analysis = AnalysisResult(
            name=name,
            age=age,
            school=school,
            subjects=sub,
            Technology=tech,
            projects=project,
            hobby=hobby,
            goal=goals,
            questionnaire_summary=q_str,
            recommendations=recom,
            general_report=explanation,
            personality_report=personality,
            overall_report=overall
            
      )
      analysis.save()  
      return redirect('result')

    return render(request, 'pages/youtube.html', {'latest_analysis_result': last_uploaded_text})

@login_required(login_url='/accounts/login/')
def result(request):
    # Retrieve the latest object from the database (replace YourModel with your actual model)
    latest_object = AnalysisResult.objects.latest('uploaded_at')  # Replace 'upload_date' with the actual date field in your model
    recommendations_list = latest_object.recommendations.split(', ')
    return render(request, 'pages/result.html', {"latest_object": latest_object, "recommendations_list": recommendations_list,})
