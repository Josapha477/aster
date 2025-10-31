# SocialApp - Plateforme Sociale

Une application web de réseau social moderne permettant le partage de contenu média et la vente de produits.

## Fonctionnalités

### 🔐 Authentification
- Inscription avec création automatique de profil
- Connexion sécurisée avec JWT tokens
- Déconnexion

### 👤 Profil Utilisateur
- Photo de profil personnalisable
- Bio (max 50 caractères)
- Visualisation de tous vos posts (média et vente)
- Modification du profil en temps réel

### 📸 Posts Média
- Upload d'images
- Description textuelle
- Affichage dans le fil d'actualité
- Tri par date de création

### 🛒 Posts Vente
- Upload d'image du produit
- Description et prix en FCFA
- Numéro WhatsApp pour contact direct
- Bouton de contact WhatsApp intégré

## Stack Technique

### Backend
- **Django 5.2.7** - Framework web Python
- **Django REST Framework** - API REST
- **djangorestframework-simplejwt** - Authentification JWT
- **Pillow** - Traitement d'images
- **django-cors-headers** - Gestion CORS
- **SQLite** - Base de données (développement)

### Frontend
- **Vue.js 3** (CDN) - Framework JavaScript progressif
- **Tailwind CSS** (CDN) - Framework CSS utility-first
- **Axios** - Client HTTP pour les requêtes API

## Installation et Démarrage

### Prérequis
- Python 3.11+

### Démarrage rapide
```bash
# Le serveur se lance automatiquement sur Replit
# Accédez à l'application via le webview
```

### Commandes utiles
```bash
# Créer des migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur pour l'admin
python manage.py createsuperuser

# Démarrer le serveur
python manage.py runserver 0.0.0.0:5000
```

## Structure du Projet

```
.
├── api/                    # Application Django principale
│   ├── migrations/         # Migrations de base de données
│   ├── models.py          # Modèles de données
│   ├── serializers.py     # Serializers DRF
│   ├── views.py           # Vues API
│   ├── urls.py            # URLs API
│   └── admin.py           # Configuration admin
├── backend/               # Configuration Django
│   ├── settings.py        # Paramètres du projet
│   └── urls.py            # URLs principales
├── templates/             # Templates HTML
│   └── index.html         # SPA Vue.js
├── media/                 # Fichiers uploadés
│   ├── profil/           # Photos de profil
│   ├── imgM/             # Images posts média
│   └── imgV/             # Images posts vente
└── manage.py             # Script de gestion Django
```

## API Endpoints

### Authentification
- `POST /api/register/` - Inscription
- `POST /api/login/` - Connexion (retourne access et refresh tokens)
- `POST /api/token/refresh/` - Rafraîchir le token
- `POST /api/logout/` - Déconnexion

### Profil
- `GET /api/profil/` - Récupérer le profil de l'utilisateur connecté
- `PATCH /api/profil/` - Mettre à jour le profil (bio, photo)

### Posts
- `GET /api/posts/media/` - Liste tous les posts média
- `POST /api/posts/media/` - Créer un post média (authentifié)
- `GET /api/posts/vente/` - Liste tous les posts vente
- `POST /api/posts/vente/` - Créer un post vente (authentifié)
- `GET /api/my-posts/` - Récupérer les posts de l'utilisateur connecté

## Utilisation

### 1. Page d'Inscription
- Cliquez sur "Inscription" dans la navigation
- Entrez un nom d'utilisateur et un mot de passe
- Un profil est automatiquement créé lors de l'inscription

### 2. Page de Connexion
- Utilisez vos identifiants pour vous connecter
- Vous serez redirigé vers le fil d'actualité

### 3. Fil d'Actualité (Accueil)
- Consultez les posts média et vente de tous les utilisateurs
- Basculez entre les onglets "Posts Média" et "Posts Vente"
- Cliquez sur le bouton WhatsApp pour contacter un vendeur

### 4. Page Profil
- Modifiez votre bio et photo de profil
- Créez de nouveaux posts (média ou vente)
- Consultez tous vos posts dans l'onglet "Mes Publications"

## Design Responsive

L'application est entièrement responsive :
- **Desktop** : Navigation horizontale avec menu complet
- **Mobile** : Menu hamburger avec navigation adaptative
- **Tablette** : Disposition en grille adaptative

## Sécurité

- Mots de passe hashés avec l'algorithme Django par défaut
- Authentification JWT avec tokens d'accès (24h) et de rafraîchissement (7 jours)
- CORS configuré pour le développement
- Validation des données côté serveur
- Upload d'images sécurisé avec Pillow

## Interface Admin Django

Accédez à l'interface d'administration Django :
- URL : `/admin/`
- Créez un superutilisateur avec : `python manage.py createsuperuser`
- Gérez les utilisateurs, profils, et posts depuis l'interface admin

## Développement Futur

Fonctionnalités potentielles :
- Système de likes et commentaires
- Messagerie entre utilisateurs
- Catégories pour les posts vente
- Recherche et filtres avancés
- Galerie multi-images par post
- Notifications en temps réel
- Mode sombre
- Support multilingue

## Licence

Ce projet est un projet éducatif de démonstration.
# aster
