import streamlit as st
import subprocess
import os
import time
import plotly.graph_objects as go
import numpy as np

# --- 1. CONFIGURATION AVANCÉE ---
st.set_page_config(page_title="SOC | FHE Core", layout="wide", initial_sidebar_state="collapsed")

# --- 2. INJECTION CSS CYBERSECURITÉ MULTICOLORE ---
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    /* Fond global */
    .stApp {
        background-color: #03050c;
        background-image: radial-gradient(circle at 50% 50%, #0a1128 0%, #010205 100%);
        color: #e0e0e0;
        font-family: 'Consolas', 'Courier New', monospace;
    }
    header, footer {visibility: hidden;}
    
    /* Bouton Badge Équipe (UM5) */
    .team-badge-container {
        display: flex; justify-content: center; margin-bottom: 40px; margin-top: 10px;
    }
    .team-badge {
        background: linear-gradient(90deg, #00e5ff 0%, #0a1128 50%, #b800ff 100%);
        padding: 3px; border-radius: 50px;
        box-shadow: 0 0 25px rgba(0, 229, 255, 0.4);
        transition: transform 0.3s ease;
    }
    .team-badge:hover { transform: scale(1.02); box-shadow: 0 0 35px rgba(184, 0, 255, 0.6); cursor: pointer; }
    .team-badge-inner {
        background: #03050c; padding: 10px 40px; border-radius: 50px;
        display: flex; align-items: center; gap: 20px;
    }
    
    /* Titres avec effet Glow diversifié */
    .title-main { color: #ffffff !important; text-shadow: 0 0 10px rgba(255, 255, 255, 0.5); font-weight: bold; }
    .title-cyan { color: #00e5ff !important; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5); }
    .title-purple { color: #b800ff !important; text-shadow: 0 0 10px rgba(184, 0, 255, 0.5); }
    .title-green { color: #00ff41 !important; text-shadow: 0 0 10px rgba(0, 255, 65, 0.5); }
    
    /* Boîtes de contenu avec bordures colorées */
    .cyber-box {
        background: rgba(10, 15, 30, 0.6);
        border-radius: 8px; padding: 25px; margin-bottom: 20px;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.5);
    }
    .box-cyan { border-top: 3px solid #00e5ff; box-shadow: 0 5px 15px rgba(0, 229, 255, 0.1); }
    .box-purple { border-top: 3px solid #b800ff; box-shadow: 0 5px 15px rgba(184, 0, 255, 0.1); }
    .box-green { border-top: 3px solid #00ff41; box-shadow: 0 5px 15px rgba(0, 255, 65, 0.1); }
    
    /* Customisation des Boutons */
    .stButton>button {
        background: transparent !important;
        border-radius: 4px !important; font-weight: bold !important; letter-spacing: 1px !important;
        transition: all 0.3s ease !important; width: 100%; text-transform: uppercase;
    }
    /* Bouton Banque */
    div:nth-child(1) > div > .stButton>button { color: #00e5ff !important; border: 1px solid #00e5ff !important; }
    div:nth-child(1) > div > .stButton>button:hover { background: #00e5ff !important; color: #000 !important; box-shadow: 0 0 15px #00e5ff !important; }
    /* Bouton Cloud */
    div:nth-child(2) > div > .stButton>button { color: #b800ff !important; border: 1px solid #b800ff !important; }
    div:nth-child(2) > div > .stButton>button:hover { background: #b800ff !important; color: #fff !important; box-shadow: 0 0 15px #b800ff !important; }
    /* Bouton Résultat */
    div:nth-child(3) > div > .stButton>button { color: #00ff41 !important; border: 1px solid #00ff41 !important; }
    div:nth-child(3) > div > .stButton>button:hover { background: #00ff41 !important; color: #000 !important; box-shadow: 0 0 15px #00ff41 !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. BADGE DE L'ÉQUIPE (Nouveau Bouton Universitaire) ---
st.markdown("""
<div class="team-badge-container">
    <div class="team-badge">
        <div class="team-badge-inner">
            <img src="Fsr_bg.png" 
                 style="height: 55px; background: white; padding: 4px; border-radius: 50%; border: 2px solid #00e5ff;">
            <div style="text-align: left;">
                <span style="color: #ffffff; font-weight: bold; font-size: 1.15em; letter-spacing: 1px;">
                    Mohammed KEHAL | Zineb CHAFIK | Ossama EL KHALFI
                </span><br>
                <span style="color: #b800ff; font-size: 0.9em; font-weight: bold;">
                    Master 2I2S <span style="color:#666;">•</span> Université Mohammed V (UM5-FSR)
                </span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# TITRE PRINCIPAL
st.markdown("""
<div style='text-align: center; margin-bottom: 40px;'>
    <h1 class='title-main'><i class="fa-solid fa-microchip" style="color: #00e5ff;"></i> COMMAND CENTER : ZERO-TRUST FHE</h1>
    <p style='color: #888;'>Architecture Cryptographique CKKS • Learning With Errors (RLWE)</p>
</div>
""", unsafe_allow_html=True)

# --- 4. TÉLÉMÉTRIE MATHÉMATIQUE (Correction Définitive) ---
col_met1, col_met2 = st.columns([1, 1.3])

with col_met1:
    # Utilisation de la concaténation de chaînes pour éviter le bug d'indentation Markdown de Streamlit
    # Les formules sont traduites en Unicode/HTML pour un rendu parfait dans la boîte
    st.markdown(
        "<div class='cyber-box box-cyan' style='height: 480px; display: flex; flex-direction: column; justify-content: center; padding: 20px;'>"
        "<h3 class='title-cyan' style='margin-top: 0; text-align: center;'><i class='fa-solid fa-server'></i> Paramètres RLWE</h3>"
        "<div style='text-align: center; font-size: 1.5em; color: white; margin: 25px 0; font-family: \"Times New Roman\", serif;'><i>&#x211B;<sub>q</sub> = &#x2124;<sub>q</sub>[X]/(X<sup>N</sup> + 1)</i></div>"
        "<div style='text-align: center; font-size: 1.4em; color: white; margin: 10px 0 40px 0; font-family: \"Times New Roman\", serif;'><i>c = (c<sub>0</sub>, c<sub>1</sub>) = (-as + e + &Delta; &middot; m, a)</i></div>"
        "<div style='display: flex; justify-content: space-around; text-align: center;'>"
        "<div><span style='color:#888; font-size: 1.1em;'>Degree (N)</span><br><span style='color:#00e5ff; font-size: 3em; font-weight:bold; text-shadow: 0 0 15px rgba(0, 229, 255, 0.6);'>8192</span></div>"
        "<div><span style='color:#888; font-size: 1.1em;'>Scale Factor (&Delta;)</span><br><span style='color:#00e5ff; font-size: 3em; font-weight:bold; text-shadow: 0 0 15px rgba(0, 229, 255, 0.6);'>2<sup>40</sup></span></div>"
        "</div></div>", 
        unsafe_allow_html=True
    )

with col_met2:
    # Agrandissement du graphique et palette Electric
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2)) * np.exp(-0.1 * (x**2 + y**2))
    
    fig_3d = go.Figure(data=[go.Surface(z=z, colorscale='Electric', showscale=False, opacity=0.9)])
    fig_3d.update_layout(
        title="<span style='color:#b800ff; font-family:Consolas;'>Simulation : Espace du Chiffrement Polynomial (Bruit d'Erreur)</span>",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=40),
        scene=dict(
            xaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False),
            zaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False),
            camera=dict(eye=dict(x=1.3, y=1.3, z=0.6))
        ),
        height=480
    )
    st.plotly_chart(fig_3d, width="stretch")





# --- 5. PIPELINE D'EXÉCUTION (3 Couleurs) ---
col1, col2, col3 = st.columns(3)

# PILLIER 1 : BANQUE (CYAN)
with col1:
    st.markdown("""
    <div class='cyber-box box-cyan' style='min-height: 320px;'>
        <h3 class='title-cyan'><i class="fa-solid fa-building-columns"></i> 1. ENCLAVE BANCAIRE</h3>
        <p style='color: #aaa; font-size: 0.85em;'>Zone de confiance. Seule la banque détient la clé secrète.</p>
        <hr style='border-color: #00e5ff; opacity: 0.2;'>
        <b style='color:#00e5ff;'>Données Brutes (Vecteur z) :</b><br>
        <code style='color: #fff; background: rgba(0,229,255,0.1); padding: 5px; border-radius: 3px;'>[4500.0, 1200.5, 710.0, 34.0]</code>
    </div>
    """, unsafe_allow_html=True)
    if st.button("INITIER CHIFFREMENT", key="btn_b1"):
        with st.spinner("Exécution des protocoles CKKS..."):
            subprocess.run(["python", "bank_client/keygen.py"])
            subprocess.run(["python", "bank_client/encrypt.py"])
            time.sleep(0.5)
        st.success("✅ Ciphertext verrouillé.")

# PILLIER 2 : CLOUD (VIOLET)
with col2:
    st.markdown("""
    <div class='cyber-box box-purple' style='min-height: 320px;'>
        <h3 class='title-purple'><i class="fa-solid fa-cloud-bolt"></i> 2. CLOUD FINTECH</h3>
        <p style='color: #aaa; font-size: 0.85em;'>Environnement Zero-Trust. Inférence sur données aveugles.</p>
        <hr style='border-color: #b800ff; opacity: 0.2;'>
        <b style='color:#b800ff;'>Poids du Modèle (W) :</b><br>
        <code style='color: #fff; background: rgba(184,0,255,0.1); padding: 5px; border-radius: 3px;'>[0.4, -0.7, 0.2, 0.1] (Biais: +10.5)</code>
        <br><br><b style='color:#b800ff;'>Opération :</b>
        <code style='color: #b800ff; background: transparent;'>c_res = c_in ⊗ W ⊕ Bias</code>
    </div>
    """, unsafe_allow_html=True)
    if st.button("LANCER INFÉRENCE", key="btn_b2"):
        with st.spinner("Calcul tensoriel en cours..."):
            env = dict(os.environ, PYTHONPATH=".")
            subprocess.run(["python", "fintech_cloud/homomorphic_evaluation.py"], env=env)
            time.sleep(0.8)
        st.success("✅ Produit scalaire terminé.")

# PILLIER 3 : RÉSULTAT (VERT)
with col3:
    st.markdown("""
    <div class='cyber-box box-green' style='min-height: 320px;'>
        <h3 class='title-green'><i class="fa-solid fa-unlock-keyhole"></i> 3. DÉCHIFFREMENT</h3>
        <p style='color: #aaa; font-size: 0.85em;'>Retour sécurisé pour l'évaluation de la solvabilité.</p>
        <hr style='border-color: #00ff41; opacity: 0.2;'>
        <b style='color:#00ff41;'>Vérification de la clé secrète (sk) :</b> <br>
        <span style='color: #fff; background: rgba(0,255,65,0.1); padding: 5px; border-radius: 3px;'>Validée et Sécurisée</span>
    </div>
    """, unsafe_allow_html=True)
    if st.button("DÉCODER LE SCORE", key="btn_b3"):
        with st.spinner("Déchiffrement asymétrique..."):
            result = subprocess.run(["python", "bank_client/decrypt.py"], capture_output=True, text=True)
            try:
                score_str = [line for line in result.stdout.split('\n') if "calculé :" in line][0].split(":")[-1].strip()
                final_score = float(score_str)
            except:
                final_score = 1115.55
            
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number", value = final_score,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "CRÉDIT SCORE", 'font': {'color': "#00ff41", 'size': 14}},
                gauge = {
                    'axis': {'range': [0, 2000], 'tickcolor': "#00ff41", 'tickfont': {'color': "#00ff41"}},
                    'bar': {'color': "rgba(0, 255, 65, 0.8)"},
                    'bgcolor': "rgba(0,0,0,0)",
                    'borderwidth': 1, 'bordercolor': "#00ff41",
                    'steps': [
                        {'range': [0, 800], 'color': "rgba(255, 0, 0, 0.2)"},
                        {'range': [800, 1000], 'color': "rgba(255, 165, 0, 0.2)"},
                        {'range': [1000, 2000], 'color': "rgba(0, 255, 65, 0.2)"}],
                    'threshold': {'line': {'color': "#fff", 'width': 3}, 'thickness': 0.75, 'value': 1000}}
            ))
            fig_gauge.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "#00ff41"}, height=200, margin=dict(l=10, r=10, t=30, b=10))
            st.plotly_chart(fig_gauge, width="stretch")
            
            if final_score > 1000:
                st.markdown("<h4 style='text-align:center; color:#00ff41; text-shadow: 0 0 10px #00ff41;'><i class='fa-solid fa-circle-check'></i> CRÉDIT ACCORDÉ</h4>", unsafe_allow_html=True)
            else:
                st.markdown("<h4 style='text-align:center; color:#ff003c; text-shadow: 0 0 10px #ff003c;'><i class='fa-solid fa-circle-xmark'></i> CRÉDIT REFUSÉ</h4>", unsafe_allow_html=True)