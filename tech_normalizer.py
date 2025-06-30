"""
Technology Normalizer - Handles synonym mapping for technology names
"""

hosting_synonyms = {
    # Basic hosting platforms
    "netlify": "Netlify",
    "vercel": "Vercel",
    "heroku": "Heroku",
    "render": "Render",
    "render.com": "Render",
    "railway": "Railway",
    "railway.app": "Railway",
    "fly.io": "Fly.io",
    "github pages": "GitHub Pages",
    "github.com": "GitHub Pages",
    "firebase hosting": "Firebase Hosting",
    "firebase": "Firebase",
    "cloudflare pages": "Cloudflare Pages",
    "cloudflare": "Cloudflare",
    
    # AWS services
    "aws": "AWS",
    "amazon web services": "AWS",
    "amazon web services (aws)": "AWS",
    "aws (amazon web services)": "AWS",
    "ec2": "AWS EC2",
    "aws ec2": "AWS EC2",
    "amazon ec2": "AWS EC2",
    "aws ec2 instances": "AWS EC2",
    "aws ec2 instance": "AWS EC2",
    "ec2 instances": "AWS EC2",
    "ec2 instance": "AWS EC2",
    "s3": "AWS S3",
    "aws s3": "AWS S3",
    "amazon s3": "AWS S3",
    "aws s3 + cloudfront": "AWS S3 + CloudFront",
    "s3 + cloudfront": "AWS S3 + CloudFront",
    "cloudfront": "AWS CloudFront",
    "aws cloudfront": "AWS CloudFront",
    "amazon cloudfront": "AWS CloudFront",
    "cloudfront cdn": "AWS CloudFront",
    "aws fargate": "AWS Fargate",
    "fargate": "AWS Fargate",
    "ecs": "AWS ECS",
    "aws ecs": "AWS ECS",
    "amazon ecs": "AWS ECS",
    "aws ecs fargate": "AWS ECS Fargate",
    "ecs fargate": "AWS ECS Fargate",
    "aws ecs (fargate)": "AWS ECS Fargate",
    "eks": "AWS EKS",
    "aws eks": "AWS EKS",
    "amazon eks": "AWS EKS",
    "rds": "AWS RDS",
    "aws rds": "AWS RDS",
    "amazon rds": "AWS RDS",
    "lambda": "AWS Lambda",
    "aws lambda": "AWS Lambda",
    "lambda functions": "AWS Lambda",
    "aws elastic beanstalk": "AWS Elastic Beanstalk",
    "elastic beanstalk": "AWS Elastic Beanstalk",
    "aws amplify": "AWS Amplify",
    "aws app runner": "AWS App Runner",
    "aws api gateway": "AWS API Gateway",
    "api gateway": "AWS API Gateway",
    "aws elb": "AWS ELB",
    "elb": "AWS ELB",
    "aws alb": "AWS ALB",
    "alb": "AWS ALB",
    "application load balancer": "AWS ALB",
    "aws application load balancer": "AWS ALB",
    "aws route 53": "AWS Route 53",
    "route 53": "AWS Route 53",
    "route53": "AWS Route 53",
    
    # Google Cloud
    "gcp": "Google Cloud Platform",
    "google cloud platform": "Google Cloud Platform",
    "google cloud": "Google Cloud Platform",
    "google cloud run": "Google Cloud Run",
    "google app engine": "Google App Engine",
    "google kubernetes engine": "Google Kubernetes Engine",
    "gke": "Google Kubernetes Engine",
    "google compute engine": "Google Compute Engine",
    "compute engine": "Google Compute Engine",
    
    # Microsoft Azure
    "azure": "Microsoft Azure",
    "microsoft azure": "Microsoft Azure",
    "azure vm": "Azure VM",
    "azure aks": "Azure AKS",
    
    # DigitalOcean
    "digitalocean": "DigitalOcean",
    "digital ocean": "DigitalOcean",
    "digitalocean droplets": "DigitalOcean Droplets",
    "digitalocean droplet": "DigitalOcean Droplets",
    "digitalocean app platform": "DigitalOcean App Platform",
    "digital ocean app platform": "DigitalOcean App Platform",
    
    # Container orchestration
    "kubernetes": "Kubernetes",
    "k8s": "Kubernetes",
    "docker": "Docker",
    "docker containers": "Docker",
    "docker compose": "Docker Compose",
    
    # Database hosting
    "mongodb atlas": "MongoDB Atlas",
    "atlas": "MongoDB Atlas",
    "supabase": "Supabase",
    "neon": "Neon",
    "neon.tech": "Neon",
    "planetscale": "PlanetScale",
    "upstash": "Upstash",
    
    # CDN and edge
    "cloudflare cdn": "Cloudflare CDN",
    "cloudflare workers": "Cloudflare Workers",
    "aws cloudfront cdn": "AWS CloudFront",
    
    # IPFS and decentralized
    "ipfs": "IPFS",
    "fleek": "Fleek",
    "fleek.co": "Fleek",
    "pinata": "Pinata",
    "pinata.cloud": "Pinata",
    
    # VPS providers
    "linode": "Linode",
    "vultr": "Vultr",
    
    # App stores
    "app store": "App Store",
    "google play store": "Google Play Store",
}

frontend_styling_synonyms = {
        # Tailwind CSS variants
        "tailwind": "Tailwind CSS",
        "tailwindcss": "Tailwind CSS",
        "tailwind css": "Tailwind CSS",
        
        # Material UI variants
        "material-ui": "Material-UI",
        "material ui": "Material-UI",
        "material-ui (mui)": "Material-UI",
        "mui (material-ui)": "Material-UI",
        "mui (material ui)": "Material-UI",
        "mui": "Material-UI",
        
        # CSS variants
        "css": "CSS",
        "css3": "CSS",
        "vanilla css": "CSS",
        "plain css": "CSS",
        "custom css": "CSS",
        "basic css": "CSS",
        "vanilla css3": "CSS",
        "html/css": "CSS",
        "html + css": "CSS",
        "pure html, css": "CSS",
        "plain html, css": "CSS",
        
        # Styled Components variants
        "styled components": "Styled Components",
        "styled-components": "Styled Components",
        "styled-components": "Styled Components",
        "css-in-js with styled components": "Styled Components",
        "css-in-js with styled-components": "Styled Components",
        "css-in-js (styled-components)": "Styled Components",
        "css-in-js (styled components)": "Styled Components",
        "styled-components for css-in-js": "Styled Components",
        "css (styled components)": "Styled Components",
        "css with styled-components": "Styled Components",
        "css/styled components": "Styled Components",
        "css/styled-components": "Styled Components",
        
        # CSS Modules variants
        "css modules": "CSS Modules",
        "css modules with scss": "CSS Modules",
        "css modules/sass": "CSS Modules",
        "plain css modules": "CSS Modules",
        "module css": "CSS Modules",
        
        # Bootstrap variants
        "bootstrap": "Bootstrap",
        "bootstrap 5": "Bootstrap",
        "css/bootstrap": "Bootstrap",
        
        # Chakra UI variants
        "chakra ui": "Chakra UI",
        "chakra ui or material ui": "Chakra UI",
        "chakra ui's styling props and theme customization": "Chakra UI",
        
        # Ant Design
        "ant design": "Ant Design",
        
        # Shadcn UI variants
        "shadcn ui": "Shadcn UI",
        "shadcn/ui": "Shadcn UI",
        "shadcn ui (with radix ui)": "Shadcn UI",
        "shadcn ui components": "Shadcn UI",
        "tailwind css with shadcn ui components": "Shadcn UI + Tailwind CSS",
        "tailwind css with shadcn ui": "Shadcn UI + Tailwind CSS",
        "tailwind css with shadcn/ui components": "Shadcn UI + Tailwind CSS",
        "tailwind css with shadcn/ui component library": "Shadcn UI + Tailwind CSS",
        
        # Headless UI variants
        "headless ui": "Headless UI",
        "headlessui": "Headless UI",
        "headless ui components": "Headless UI",
        "tailwind css (with headless ui)": "Headless UI + Tailwind CSS",
        "tailwind css with headless ui": "Headless UI + Tailwind CSS",
        "tailwind css with headless ui components": "Headless UI + Tailwind CSS",
        "tailwind css with headlessui components": "Headless UI + Tailwind CSS",
        "tailwind css with headlessui": "Headless UI + Tailwind CSS",
        "tailwind + headless ui": "Headless UI + Tailwind CSS",
        
        # DaisyUI variants
        "daisyui": "DaisyUI",
        "daisyui component library": "DaisyUI",
        "daisyui components": "DaisyUI",
        "tailwind css with daisyui components": "DaisyUI + Tailwind CSS",
        "tailwind css with daisyui": "DaisyUI + Tailwind CSS",
        "tailwind css with daisyui": "DaisyUI + Tailwind CSS",
        
        # Emotion variants
        "emotion": "Emotion",
        "css-in-js with emotion": "Emotion",
        "css-in-js with emotion or styled-components": "Emotion",
        "styled-components/emotion": "Emotion",
        
        # Sass/SCSS variants
        "sass": "Sass",
        "scss": "SCSS",
        "css/scss": "SCSS",
        "plain css/scss": "SCSS",
        
        # CSS-in-JS generic
        "css-in-js": "CSS-in-JS",
        "css-in-js via material ui's styling solution": "CSS-in-JS",
        "css-in-js with material-ui's styling solution": "CSS-in-JS",
        "css-in-js solutions like styled components": "CSS-in-JS",
        "css-in-js libraries like styled components": "CSS-in-JS",
        "css-in-js libraries like styled components or emotion": "CSS-in-JS",
        "css-in-js with styled components or emotion": "CSS-in-JS",
        "css-in-js approach with a lightweight solution": "CSS-in-JS",
        "css-in-js (e.g., styled-components)": "CSS-in-JS",
        "css-in-js (e.g., emotion or styled components) or css variables": "CSS-in-JS",
        
        # Mantine variants
        "mantine": "Mantine",
        "mantine ui": "Mantine",
        
        # Radix UI
        "radix ui": "Radix UI",
        
        # Other styling solutions
        "pico.css": "Pico.css",
        "flowbite": "Flowbite",
        "picnic css": "Picnic CSS",
        "framer motion": "Framer Motion",
        "shadow dom": "Shadow DOM",
        "css variables": "CSS Variables",
        "css grid": "CSS Grid",
        "flexbox": "Flexbox",
        "css flexbox": "Flexbox",
        "grid": "Grid",
        "css media queries": "CSS Media Queries",
        
        # React Native specific
        "react native elements": "React Native Elements",
        "nativebase": "NativeBase",
        "native base": "NativeBase",
        "react native paper": "React Native Paper",
        "tailwind css with nativewind": "NativeWind",
        
        # HTML variants
        "html": "HTML",
        "html5": "HTML5",
        "html/css/javascript": "HTML/CSS/JavaScript",
        
        # Combinations and custom
        "custom components": "Custom Components",
        "tailwind css with custom components": "Tailwind CSS + Custom",
        "tailwind css with a custom design system": "Tailwind CSS + Custom",
        "tailwind css with a component library like shadcn ui": "Tailwind CSS + Components",
        "material ui with custom academic-themed styling": "Material-UI + Custom",
        "material ui with custom theming": "Material-UI + Custom",
        "material ui with a custom theming system": "Material-UI + Custom",
        "material ui with custom styling": "Material-UI + Custom",
        "tailwind css + tremor": "Tailwind CSS + Tremor",
        
        # Null/None values
        "none": "None",
        "null": "None",
        
        # Add more styling synonyms as needed...
    }

frontend_frameworks_synonyms = {
    # React variants
    "react": "React",
    "reactjs": "React",
    "react.js": "React",
    "react js": "React",
    "react with typescript": "React",
    "react.js with typescript": "React",
    "react (with typescript)": "React",
    "react.js (with typescript)": "React",
    "react with hooks": "React",
    "react (with hooks)": "React",
    "react 18": "React",
    "react 18+": "React",
    "react 18.x": "React",
    "create react app": "React",
    "react (with vite)": "React",
    "react.js (via vite)": "React",
    "react.js with vite": "React",
    "react with typescript + vite": "React",
    "react + typescript": "React",
    "react (with typescript) & next.js": "React",
    "react with typescript (using next.js)": "React",
    "react with typescript (next.js)": "React",
    "react with typescript + vite": "React",
    
    # Next.js variants
    "next.js": "Next.js",
    "nextjs": "Next.js",
    "next": "Next.js",
    "next.js 14+": "Next.js",
    "next.js 13+": "Next.js",
    "next.js 14": "Next.js",
    "next.js (react)": "Next.js",
    "next.js (react framework)": "Next.js",
    "next.js (react.js)": "Next.js",
    "next.js (with react)": "Next.js",
    "next.js (with react.js)": "Next.js",
    "next.js (with react & typescript)": "Next.js",
    "next.js (with react.js and typescript)": "Next.js",
    "next.js (with react.js & typescript)": "Next.js",
    "next.js (react framework) with typescript": "Next.js",
    "next.js (react.js framework)": "Next.js",
    "next.js (react.js with typescript)": "Next.js",
    "next.js (react, typescript)": "Next.js",
    "next.js (react with typescript)": "Next.js",
    "next.js (react-based)": "Next.js",
    "next.js (built on react)": "Next.js",
    "next.js (with static site generation - ssg)": "Next.js",
    "next.js (react) in static site generation (ssg) mode": "Next.js",
    "next.js with typescript": "Next.js",
    "next.js (react framework)": "Next.js",
    "react.js with next.js": "Next.js",
    "react with next.js": "Next.js",
    "react (with next.js)": "Next.js",
    "react with next.js 14": "Next.js",
    "react with next.js (typescript)": "Next.js",
    "react.js with next.js (typescript)": "Next.js",
    "react (with next.js framework)": "Next.js",
    "react.js (with next.js)": "Next.js",
    "react.js (with next.js for web)": "Next.js",
    
    # Vue.js variants
    "vue": "Vue.js",
    "vuejs": "Vue.js",
    "vue.js": "Vue.js",
    "vue js": "Vue.js",
    "vue.js 3": "Vue.js",
    "vue 3": "Vue.js",
    "vue 3 from a cdn": "Vue.js",
    
    # Angular variants
    "angular": "Angular",
    "angularjs": "Angular",
    "angular js": "Angular",
    
    # Svelte variants
    "svelte": "Svelte",
    "sveltekit": "SvelteKit",
    "svelte with sveltekit": "SvelteKit",
    
    # Other frameworks
    "astro": "Astro",
    "hugo": "Hugo",
    "jekyll": "Jekyll",
    "eleventy (11ty)": "Eleventy",
    "11ty": "Eleventy",
    "vite": "Vite",
    
    # React Native variants
    "react native": "React Native",
    "react-native": "React Native",
    "react native with expo": "React Native",
    "react native (for mobile)": "React Native",
    "react native (typescript)": "React Native",
    
    # Electron variants
    "electron": "Electron",
    "electron.js": "Electron",
    "electronjs": "Electron",
    
    # Game engines and 3D
    "unity": "Unity",
    "unity 3d": "Unity",
    "a-frame": "A-Frame",
    "react three fiber": "React Three Fiber",
    "react vr": "React VR",
    "react 360": "React 360",
    "webxr": "WebXR",
    "webxr api": "WebXR API",
    "your own engine (standalone)": "Custom Engine",
    
    # Mobile frameworks
    "flutter": "Flutter",
    
    # TypeScript (when used as framework context)
    "typescript": "TypeScript",
    
    # Template engines
    "jinja2": "Jinja2",
    "django templates": "Django Templates",
    "server-rendered html": "Server-Rendered HTML",
    
    # Other libraries that might be categorized as frameworks
    "htmx": "HTMX",
    "alpine.js": "Alpine.js",
    "alpinejs": "Alpine.js",
    "redux toolkit": "Redux Toolkit",
    "react router": "React Router",
    "react-router-dom": "React Router",
    "react hook form": "React Hook Form",
    "react query": "React Query",
    
    # Add more frontend framework synonyms as needed...
}

frontend_libraries_synonyms = {
    # Material-UI variants
    "material ui": "Material-UI",
    "material-ui": "Material-UI",
    "material-ui (mui)": "Material-UI",
    "mui (material-ui)": "Material-UI",
    "mui (material ui)": "Material-UI",
    "mui": "Material-UI",
    
    # Redux variants
    "redux": "Redux",
    "redux toolkit": "Redux Toolkit",
    "redux-toolkit": "Redux Toolkit",
    "redux toolkit (rtk query)": "Redux Toolkit",
    "redux toolkit (with rtk query)": "Redux Toolkit",
    "rtk query": "RTK Query",
    "redux-saga": "Redux-Saga",
    "react-redux": "React-Redux",
    "redux with redux toolkit": "Redux Toolkit",
    
    # Axios variants
    "axios": "Axios",
    
    # Chart libraries
    "chart.js": "Chart.js",
    "charts.js": "Chart.js",
    "recharts": "Recharts",
    "d3.js": "D3.js",
    "d3": "D3.js",
    "d3.js (d3.js v7+)": "D3.js",
    "d3.js with recharts": "D3.js + Recharts",
    "nivo": "Nivo",
    "nivo charts": "Nivo",
    "nivo.rocks": "Nivo",
    "echarts": "ECharts",
    "echarts.js": "ECharts",
    "apache echarts": "ECharts",
    "apache echarts": "ECharts",
    "plotly.js": "Plotly.js",
    "plotly": "Plotly",
    "plotly.js / react-plotly.js": "Plotly.js",
    "plotly.js (with react-plotly.js wrapper)": "Plotly.js",
    "react-chartjs-2": "React-Chartjs-2",
    "react-chart.js-2": "React-Chartjs-2",
    "chart.js (react-chartjs-2)": "React-Chartjs-2",
    "react chart.js 2": "React-Chartjs-2",
    "apexcharts": "ApexCharts",
    "apexcharts.js": "ApexCharts",
    "highcharts": "Highcharts",
    "victory": "Victory",
    "victory charts": "Victory",
    "tradingview lightweight charts": "TradingView Lightweight Charts",
    "lightweight charts (from tradingview)": "TradingView Lightweight Charts",
    "tradingview charts": "TradingView Charts",
    "tradingview charting library": "TradingView Charts",
    "visx": "Visx",
    "react charts": "React Charts",
    "react-vis": "React-Vis",
    
    # React Router variants
    "react router": "React Router",
    "react-router": "React Router",
    "react router dom": "React Router DOM",
    "react-router-dom": "React Router DOM",
    "react router dom": "React Router DOM",
    
    # Form libraries
    "react hook form": "React Hook Form",
    "react-hook-form": "React Hook Form",
    "react-hook-form": "React Hook Form",
    "formik": "Formik",
    "yup": "Yup",
    "yup validation": "Yup",
    "zod": "Zod",
    
    # State management
    "zustand": "Zustand",
    "jotai": "Jotai",
    "recoil": "Recoil",
    "context api": "React Context API",
    "react context api": "React Context API",
    "react context": "React Context",
    "react context api + hooks": "React Context API",
    "react context api with hooks": "React Context API",
    "usecontext": "useContext",
    "usestate": "useState",
    "usereducer": "useReducer",
    "usestate`/`usereducer` hooks": "React Hooks",
    "usestate hooks": "React Hooks",
    "react hooks": "React Hooks",
    
    # UI Component Libraries
    "chakra ui": "Chakra UI",
    "ant design": "Ant Design",
    "headless ui": "Headless UI",
    "headlessui": "Headless UI",
    "headless ui components": "Headless UI",
    "headlessui components": "Headless UI",
    "headless ui library": "Headless UI",
    "@headlessui/react": "Headless UI",
    "tailwind css with headless ui components": "Headless UI",
    "tailwind css with headless ui": "Headless UI",
    "headless ui components": "Headless UI",
    "radix ui": "Radix UI",
    "radix ui primitives": "Radix UI",
    "radix ui (headless components)": "Radix UI",
    "shadcn ui": "Shadcn UI",
    "shadcn/ui": "Shadcn UI",
    "shadcn ui components": "Shadcn UI",
    "shadcn/ui components": "Shadcn UI",
    "daisyui": "DaisyUI",
    "daisyui components": "DaisyUI",
    "tailwind css with daisyui components": "DaisyUI",
    "mantine ui": "Mantine",
    "mantine": "Mantine",
    "bootstrap 5": "Bootstrap",
    "bootstrap": "Bootstrap",
    
    # Data fetching
    "react query": "React Query",
    "react-query": "React Query",
    "tanstack query": "TanStack Query",
    "react query (tanstack query)": "TanStack Query",
    "tanstack query (react query)": "TanStack Query",
    "swr": "SWR",
    "apollo client": "Apollo Client",
    "apollo server": "Apollo Server",
    
    # Animation libraries
    "framer motion": "Framer Motion",
    "react spring": "React Spring",
    "lottie": "Lottie",
    "aos (animate on scroll)": "AOS",
    
    # Map libraries
    "mapbox": "Mapbox",
    "mapbox gl js": "Mapbox GL JS",
    "mapbox gl": "Mapbox GL",
    "mapboxgl js": "Mapbox GL JS",
    "mapboxgl": "Mapbox GL",
    "mapbox": "Mapbox",
    "mapbox gl js with deck.gl": "Mapbox + Deck.gl",
    "react-map-gl": "React-Map-GL",
    "react-mapbox gl js": "React-Mapbox-GL",
    "leaflet": "Leaflet",
    "leaflet.js": "Leaflet.js",
    "leafletjs": "Leaflet.js",
    "react-leaflet": "React-Leaflet",
    "leaflet.js (with react-leaflet)": "React-Leaflet",
    "leaflet.js with react-leaflet": "React-Leaflet",
    "leaflet with react-leaflet": "React-Leaflet",
    "google maps api": "Google Maps API",
    "google maps javascript api": "Google Maps JavaScript API",
    "google maps platform": "Google Maps Platform",
    "react-google-maps": "React-Google-Maps",
    "react google maps": "React Google Maps",
    "@react-google-maps/api": "React-Google-Maps",
    "react google maps library": "React Google Maps",
    "openlayers": "OpenLayers",
    "openstreetmap": "OpenStreetMap",
    "cesiumjs": "CesiumJS",
    "deck.gl": "Deck.gl",
    "turf.js": "Turf.js",
    "maplibre gl js": "MapLibre GL JS",
    
    # Socket/WebSocket libraries
    "socket.io": "Socket.IO",
    "socket.io client": "Socket.IO Client",
    "socket.io-client": "Socket.IO Client",
    "socket.io (client-side)": "Socket.IO Client",
    "socket.io (client)": "Socket.IO Client",
    "websocket": "WebSocket",
    "websockets": "WebSockets",
    "websockets api": "WebSockets API",
    "websocket api": "WebSocket API",
    "ws": "ws",
    
    # 3D/WebGL libraries
    "three.js": "Three.js",
    "threejs": "Three.js",
    "react three fiber": "React Three Fiber",
    "react-three-fiber": "React Three Fiber",
    "react three fiber (r3f)": "React Three Fiber",
    "react three fiber (with three.js)": "React Three Fiber",
    "three.js with react three fiber": "React Three Fiber",
    "three.js (with react-three-fiber)": "React Three Fiber",
    "drei": "Drei",
    "babylon.js": "Babylon.js",
    "a-frame": "A-Frame",
    "aframe.js": "A-Frame",
    "webxr": "WebXR",
    "webxr api": "WebXR API",
    "webxr device api": "WebXR Device API",
    "webvr/webxr api": "WebXR API",
    "ar.js": "AR.js",
    "8th wall": "8th Wall",
    "react-xr": "React-XR",
    "webgl": "WebGL",
    "pixi.js": "PixiJS",
    "pixijs": "PixiJS",
    "konva.js": "Konva.js",
    "react-konva": "React-Konva",
    "fabric.js": "Fabric.js",
    "paper.js": "Paper.js",
    "svg.js": "SVG.js",
    "snap.svg": "Snap.svg",
    "canvg": "canvg",
    "regl": "regl",
    "vtk.js": "VTK.js",
    
    # Web3/Blockchain libraries
    "ethers.js": "Ethers.js",
    "web3.js": "Web3.js",
    "wagmi": "Wagmi",
    "wagmi hooks": "Wagmi",
    "wagmi.sh": "Wagmi",
    "wagmi & rainbowkit": "Wagmi + RainbowKit",
    "wagmi + ethers.js": "Wagmi + Ethers.js",
    "viem": "Viem",
    "web3modal": "Web3Modal",
    "web3-modal": "Web3Modal",
    "rainbowkit": "RainbowKit",
    "walletconnect": "WalletConnect",
    "metamask": "MetaMask",
    "web3-react": "Web3-React",
    "the graph": "The Graph",
    "openzeppelin contracts": "OpenZeppelin Contracts",
    "chainlink": "Chainlink",
    
    # Date/Time libraries
    "moment.js": "Moment.js",
    "moment.js with moment-timezone": "Moment.js",
    "date-fns": "date-fns",
    "date-fns": "date-fns",
    "date-fns-tz": "date-fns-tz",
    "day.js": "Day.js",
    "luxon": "Luxon",
    
    # Calendar libraries
    "react-big-calendar": "React-Big-Calendar",
    "react big calendar": "React Big Calendar",
    "react-big-calendar": "React-Big-Calendar",
    "react calendar": "React Calendar",
    "react-calendar": "React-Calendar",
    "fullcalendar": "FullCalendar",
    "fullcalendar.js": "FullCalendar.js",
    "fullcalendar.io": "FullCalendar",
    "fullcalendar (with its react wrapper)": "FullCalendar",
    "fullcalendar react": "FullCalendar React",
    "fullcalendar-react": "FullCalendar React",
    "react-datepicker": "React-Datepicker",
    "react date picker": "React Date Picker",
    "mui date picker": "MUI Date Picker",
    "react-day-picker": "React-Day-Picker",
    "flatpickr": "Flatpickr",
    "react-chrono": "React-Chrono",
    "react-calendar-heatmap": "React-Calendar-Heatmap",
    
    # Drag and Drop
    "react-beautiful-dnd": "React-Beautiful-DnD",
    "react beautiful dnd": "React Beautiful DnD",
    "react-dnd": "React-DnD",
    "react dnd": "React DnD",
    "@dnd-kit": "@dnd-kit",
    "dnd-kit": "dnd-kit",
    
    # File handling
    "react-dropzone": "React-Dropzone",
    "react dropzone": "React Dropzone",
    "react-pdf": "React-PDF",
    "pdf.js": "PDF.js",
    "pdf.js (mozilla)": "PDF.js",
    "pdfjs-dist": "pdfjs-dist",
    "jspdf": "jsPDF",
    "html2canvas": "html2canvas",
    "html-to-image": "html-to-image",
    "react-to-pdf": "React-to-PDF",
    "pdfkit": "PDFKit",
    "epub.js": "EPUB.js",
    "epubjs": "EPUB.js",
    
    # Text editors
    "monaco editor": "Monaco Editor",
    "monaco-editor": "Monaco Editor",
    "codemirror": "CodeMirror",
    "codemirror 6": "CodeMirror 6",
    "quill": "Quill",
    "quill.js": "Quill.js",
    "react-quill": "React-Quill",
    "ckeditor": "CKEditor",
    "ckeditor 5": "CKEditor 5",
    "draft.js": "Draft.js",
    "slate.js": "Slate.js",
    "slate": "Slate",
    "tiptap": "TipTap",
    "tiptap (built on prosemirror)": "TipTap",
    "prosemirror": "ProseMirror",
    "lexical": "Lexical",
    "react email editor": "React Email Editor",
    "grapesjs": "GrapesJS",
    
    # Markdown
    "react-markdown": "React-Markdown",
    "marked.js": "Marked.js",
    "marked": "Marked",
    "markdown-it": "Markdown-it",
    "remark-gfm": "remark-gfm",
    "rehype-highlight": "rehype-highlight",
    "mdx": "MDX",
    
    # Syntax highlighting
    "prism.js": "Prism.js",
    "prismjs": "PrismJS",
    "highlight.js": "Highlight.js",
    "react-syntax-highlighter": "React-Syntax-Highlighter",
    "react-diff-viewer": "React-Diff-Viewer",
    "diff2html": "Diff2Html",
    
    # Video/Audio
    "video.js": "Video.js",
    "videojs": "VideoJS",
    "video.js with react wrapper": "Video.js",
    "video.js with hls.js": "Video.js + HLS.js",
    "react player": "React Player",
    "react-player": "React-Player",
    "plyr": "Plyr",
    "plyr.js": "Plyr.js",
    "plyr (with react wrapper)": "Plyr",
    "hls.js": "HLS.js",
    "react-h5-audio-player": "React-H5-Audio-Player",
    "wavesurfer.js": "WaveSurfer.js",
    "react-wavesurfer": "React-WaveSurfer",
    "howler.js": "Howler.js",
    "tone.js": "Tone.js",
    "web audio api": "Web Audio API",
    "ffmpeg.wasm": "FFmpeg.wasm",
    
    # Image/Gallery
    "react-image-gallery": "React-Image-Gallery",
    "react image gallery": "React Image Gallery",
    "react-photo-gallery": "React-Photo-Gallery",
    "react-image-crop": "React-Image-Crop",
    "react image zoom": "React Image Zoom",
    "react image compare": "React Image Compare",
    "react slick": "React Slick",
    "react swiper": "React Swiper",
    "react-device-frames": "React-Device-Frames",
    
    # Testing
    "react testing library": "React Testing Library",
    "jest": "Jest",
    "cypress": "Cypress",
    "playwright": "Playwright",
    "storybook": "Storybook",
    "jest-image-snapshot": "jest-image-snapshot",
    
    # Utilities
    "lodash": "Lodash",
    "rxjs": "RxJS",
    "fetch": "Fetch",
    "fetch api": "Fetch API",
    "jquery": "jQuery",
    "vite": "Vite",
    "webpack": "Webpack",
    "create react app": "Create React App",
    "create-react-app": "Create React App",
    "workbox": "Workbox",
    "localforage": "localForage",
    
    # Internationalization
    "i18next": "i18next",
    "react-i18next": "react-i18next",
    "react-intl": "React-Intl",
    "next-intl": "next-intl",
    
    # Notifications
    "react-toastify": "React-Toastify",
    "toastify": "Toastify",
    
    # Icons
    "heroicons": "Heroicons",
    "react-icons": "react-icons",
    "font awesome": "Font Awesome",
    
    # Search
    "fuse.js": "Fuse.js",
    "algolia instantsearch.js components": "Algolia InstantSearch",
    "react instantsearch": "React InstantSearch",
    "lunr.js": "Lunr.js",
    "simple-jekyll-search": "Simple-Jekyll-Search",
    
    # Data visualization
    "sigma.js": "Sigma.js",
    "react flow": "React Flow",
    "react-flow": "React-Flow",
    "vis.js": "Vis.js",
    "cytoscape.js": "Cytoscape.js",
    "jointjs": "JointJS",
    "gojs": "GoJS",
    "react-force-graph": "React-Force-Graph",
    "react-wordcloud": "React-Wordcloud",
    
    # Tables/Grids
    "ag-grid": "AG Grid",
    "ag grid": "AG Grid",
    "material-ui datagrid": "Material-UI DataGrid",
    "react table": "React Table",
    "react-table": "React-Table",
    "tanstack table (react table v8)": "TanStack Table",
    "react-window": "React-Window",
    "react-virtualized": "React-Virtualized",
    "react-grid-layout": "React-Grid-Layout",
    
    # Crypto/Security
    "cryptojs": "CryptoJS",
    "crypto-js": "crypto-js",
    "web crypto api": "Web Crypto API",
    "jose": "jose",
    "zxcvbn": "zxcvbn",
    "elliptic": "elliptic",
    "jsrsasign": "jsrsasign",
    
    # Collaboration
    "yjs": "Yjs",
    "y.js": "Y.js",
    "y-websocket": "y-websocket",
    "rrweb": "rrweb",
    
    # Machine Learning
    "tensorflow.js": "TensorFlow.js",
    "hugging face transformers": "Hugging Face Transformers",
    
    # Color
    "chroma.js": "Chroma.js",
    
    # Math
    "mathjs": "mathjs",
    
    # Office
    "office.js": "Office.js",
    "xlsx": "xlsx",
    
    # Swagger/API
    "swagger-parser": "swagger-parser",
    "swagger-ui-react": "swagger-ui-react",
    "swagger ui": "Swagger UI",
    "redoc": "ReDoc",
    
    # Chemistry
    "react-mol-kit": "React-Mol-Kit",
    "chemdoodle": "ChemDoodle",
    
    # Monitoring
    "launchdarkly": "LaunchDarkly",
    "grafana": "Grafana",
    
    # AWS
    "aws amplify": "AWS Amplify",
    "aws amplify js library": "AWS Amplify",
    "aws amplify libraries": "AWS Amplify",
    "aws sdk": "AWS SDK",
    "aws amplify video": "AWS Amplify Video",
    
    # Communication
    "agora.io sdk": "Agora.io SDK",
    "twilio programmable video": "Twilio Programmable Video",
    "twilio programmable video sdk": "Twilio Programmable Video SDK",
    "webrtc": "WebRTC",
    "webrtc apis": "WebRTC APIs",
    "peerjs": "PeerJS",
    "simple-peer library": "Simple-Peer",
    "mediasoup-client": "mediasoup-client",
    "ably sdk": "Ably SDK",
    
    # QR Code
    "react-qr-reader": "React-QR-Reader",
    "react-qr-code": "React-QR-Code",
    "zxing": "ZXing",
    
    # Copy to clipboard
    "react-copy-to-clipboard": "React-Copy-to-Clipboard",
    
    # JSON
    "react-json-view": "React-JSON-View",
    "react json tree": "React JSON Tree",
    "json-parse-helpfulerror": "json-parse-helpfulerror",
    "jsonlint-extended": "jsonlint-extended",
    
    # Base64
    "js-base64": "js-base64",
    
    # Regex
    "regexp-tree": "regexp-tree",
    
    # Spinners/Loading
    "react-spinners": "React-Spinners",
    
    # Intersection Observer
    "react-intersection-observer": "React-Intersection-Observer",
    
    # IPFS
    "ipfs http client": "IPFS HTTP Client",
    
    # Currency
    "dinero.js": "Dinero.js",
    
    # Image processing
    "pannellum": "Pannellum",
    "openseadragon": "OpenSeadragon",
    "cloudinary react sdk": "Cloudinary React SDK",
    
    # File upload
    "@uppy/react": "@uppy/react",
    
    # DID/Identity
    "@transmute/did-key": "@transmute/did-key",
    "did-jwt": "did-jwt",
    "did-vc": "did-vc",
    "jsonld-signatures": "jsonld-signatures",
    "uport": "uPort",
    "ethereum universal wallet sdk": "Ethereum Universal Wallet SDK",
    
    # Query Builder
    "react query builder": "React Query Builder",
    
    # BPMN
    "bpmn.io": "bpmn.io",
    "bpmn.js": "BPMN.js",
    
    # AR
    "ar foundation": "AR Foundation",
    "react native ar bridges": "React Native AR Bridges",
    
    # Browser APIs
    "browser-filesystem api": "Browser FileSystem API",
    "webhid api": "WebHID API",
    "canvas api": "Canvas API",
    "html5 video api": "HTML5 Video API",
    "webassembly (wasm)": "WebAssembly",
    "media source extensions (mse)": "Media Source Extensions",
    
    # Physics
    "rapier.js": "Rapier.js",
    "@react-three/rapier": "@react-three/rapier",
    "ammo.js": "Ammo.js",
    
    # Resize
    "react-resizable": "React-Resizable",
    
    # Other
    "blockly": "Blockly",
    "elastic ui components": "Elastic UI",
    "libsignal-protocol-javascript": "libsignal-protocol-javascript",
    "react aria": "React ARIA",
    "custom svg library": "Custom SVG Library",
    "unity ui system": "Unity UI System",
    "nextauth.js": "NextAuth.js",
    "auth0 react sdk": "Auth0 React SDK",
    "mjml": "MJML",
    "uppy": "Uppy",
    "media.js": "Media.js",
    "websocket integration": "WebSocket Integration",
    "hls.js/dash.js": "HLS.js/Dash.js",
    "vanilla javascript": "Vanilla JavaScript",
    "vanilla js": "Vanilla JavaScript",
    "vanilla javascript (es6+)": "Vanilla JavaScript",
    "javascript": "JavaScript",
    "javascript (es6+)": "JavaScript",
    "javascript (vanilla js)": "JavaScript",
    "typescript": "TypeScript",
    "html5": "HTML5",
    "css3": "CSS3",
    "html": "HTML",
    "css": "CSS",
    "svg": "SVG",
    "webextension api": "WebExtension API",
    "null": "null",
    
    # Add more frontend library synonyms as needed...
}

backend_frameworks_synonyms = {
    # Express.js variants
    "express": "Express.js",
    "expressjs": "Express.js",
    "express.js": "Express.js",
    "node.js with express": "Express.js",
    "node.js with express.js": "Express.js",
    "node.js and express": "Express.js",
    "node.js and express.js": "Express.js",
    "node.js & express": "Express.js",
    "node.js & express.js": "Express.js",
    "node.js + express": "Express.js",
    "node.js + express.js": "Express.js",
    "node.js (with express)": "Express.js",
    "node.js (with express.js)": "Express.js",
    "node.js (express.js)": "Express.js",
    "node.js (express.js framework)": "Express.js",
    "node.js/express": "Express.js",
    "node.js/express.js": "Express.js",
    "express.js (node.js)": "Express.js",
    "node.js with express (typescript)": "Express.js",
    "node.js with express.js (typescript)": "Express.js",
    "node.js with express (with typescript)": "Express.js",
    "node.js with express.js and typescript": "Express.js",
    "node.js with express.js (with typescript)": "Express.js",
    "node.js (with express.js & typescript)": "Express.js",
    "node.js with express & typescript": "Express.js",
    "express.js (with typescript)": "Express.js",
    "node.js with the express.js framework": "Express.js",
    "node.js with express.js (or fastify)": "Express.js",
    "node.js, express": "Express.js",
    "node.js (with typescript) using express.js": "Express.js",
    "node.js (with typescript) + express.js": "Express.js",
    
    # FastAPI variants
    "fastapi": "FastAPI",
    "python with fastapi": "FastAPI",
    "fastapi (python)": "FastAPI",
    "python (fastapi)": "FastAPI",
    "fastapi (with python)": "FastAPI",
    "fastapi microservice": "FastAPI",
    "python with fastapi microservice": "FastAPI",
    "python microservice using fastapi": "FastAPI",
    "python 3.x with fastapi": "FastAPI",
    "python 3.10+ with fastapi": "FastAPI",
    "fastapi (for dedicated ml endpoints)": "FastAPI",
    "python with fastapi (deployed on aws lambda via api gateway)": "FastAPI",
    
    # Django variants
    "django": "Django",
    "django rest framework": "Django REST Framework",
    "django rest framework (drf)": "Django REST Framework",
    "django (with django rest framework - drf)": "Django REST Framework",
    "django with django rest framework (drf)": "Django REST Framework",
    "django rest framework": "Django REST Framework",
    "django (with django rest framework)": "Django REST Framework",
    "python with django (and django rest framework)": "Django REST Framework",
    "python 3.x with django & django rest framework (drf)": "Django REST Framework",
    "python with django rest framework (drf)": "Django REST Framework",
    "django (python)": "Django",
    "python with django": "Django",
    "django 5.x": "Django",
    "django channels": "Django Channels",
    
    # Flask variants
    "flask": "Flask",
    "flask-restful": "Flask-RESTful",
    "flask api": "Flask API",
    "flask-blueprint": "Flask-Blueprint",
    "python with flask": "Flask",
    "python flask": "Flask",
    "flask-socketio": "Flask-SocketIO",
    "flask-migrate": "Flask-Migrate",
    "flask microservices": "Flask",
    "python (flask or fastapi)": "Flask/FastAPI",
    "python (flask/fastapi)": "Flask/FastAPI",
    "flask/fastapi": "Flask/FastAPI",
    "python (flask/celery)": "Flask + Celery",
    
    # NestJS variants
    "nestjs": "NestJS",
    "nest.js": "NestJS",
    "nestjs framework": "NestJS",
    "node.js with nestjs": "NestJS",
    "nestjs (node.js)": "NestJS",
    "nestjs (node.js framework)": "NestJS",
    "nestjs (node.js framework with typescript)": "NestJS",
    "nestjs (node.js framework) with typescript": "NestJS",
    "nestjs (node.js/typescript)": "NestJS",
    "nestjs (with node.js & typescript)": "NestJS",
    "nestjs (with node.js and typescript)": "NestJS",
    "nestjs (node.js with typescript)": "NestJS",
    "nestjs (with typescript)": "NestJS",
    "nestjs with typescript": "NestJS",
    "nestjs (typescript)": "NestJS",
    "nestjs (typescript, node.js)": "NestJS",
    "nestjs (built on node.js)": "NestJS",
    "node.js with nestjs (typescript)": "NestJS",
    "node.js with nestjs framework": "NestJS",
    "node.js with nestjs (framework)": "NestJS",
    "node.js with nestjs framework (typescript)": "NestJS",
    "node.js with nestjs (typescript-first)": "NestJS",
    "node.js with typescript (using nestjs)": "NestJS",
    "node.js with typescript (using nestjs framework)": "NestJS",
    "node.js with typescript & nestjs framework": "NestJS",
    "node.js with typescript and nestjs": "NestJS",
    "node.js (with nestjs)": "NestJS",
    "node.js (typescript) with nestjs": "NestJS",
    "typescript with nestjs": "NestJS",
    "nestjs gateways": "NestJS",
    
    # Go frameworks
    "gin": "Gin",
    "gin gonic": "Gin",
    "gin-gonic": "Gin",
    "gin framework": "Gin",
    "gin web framework": "Gin",
    "gin-gonic/gin": "Gin",
    "gin/gonic": "Gin",
    "gin web framework": "Gin",
    "echo": "Echo",
    "echo framework": "Echo",
    "fiber": "Fiber",
    "go fiber": "Fiber",
    "gin/fiber": "Gin/Fiber",
    "gorilla/mux": "Gorilla Mux",
    "gorilla mux": "Gorilla Mux",
    "chi": "Chi",
    "go's standard library (net/http)": "Go net/http",
    "go's standard library net/http": "Go net/http",
    "go's standard library": "Go Standard Library",
    "go standard library": "Go Standard Library",
    "net/http": "Go net/http",
    "hyper": "Hyper",
    
    # Spring Boot variants
    "spring boot": "Spring Boot",
    "spring boot 3+": "Spring Boot",
    "spring boot 3": "Spring Boot",
    "spring boot webflux": "Spring Boot WebFlux",
    "spring boot (java)": "Spring Boot",
    "java with spring boot": "Spring Boot",
    "spring cloud": "Spring Cloud",
    "spring boot 3+ with spring cloud": "Spring Boot + Spring Cloud",
    "spring cloud gateway": "Spring Cloud Gateway",
    "spring cloud config": "Spring Cloud Config",
    
    # Next.js API variants
    "next.js api routes": "Next.js API Routes",
    "next.js api routes (serverless functions)": "Next.js API Routes",
    "next.js api routes (serverless)": "Next.js API Routes",
    "next.js api routes (node.js)": "Next.js API Routes",
    "next.js api routes (node.js/typescript)": "Next.js API Routes",
    "next.js api routes / server components": "Next.js API Routes",
    "next.js with typescript": "Next.js",
    "next.js (react)": "Next.js",
    
    # Fastify variants
    "fastify": "Fastify",
    "fastify (with typescript)": "Fastify",
    "fastify (node.js)": "Fastify",
    "node.js (fastify)": "Fastify",
    "node.js with fastify": "Fastify",
    
    # GraphQL variants
    "graphql": "GraphQL",
    "apollo server": "Apollo Server",
    "graphql with apollo server": "Apollo Server",
    "graphql (apollo server)": "Apollo Server",
    "apollo graphql": "Apollo GraphQL",
    "graphql using apollo server": "Apollo Server",
    "graphql (with apollo server)": "Apollo Server",
    "graphql via apollo server": "Apollo Server",
    "apollo": "Apollo",
    "graphql api": "GraphQL API",
    "graphql api (with strawberry for python)": "GraphQL + Strawberry",
    "strawberry graphql": "Strawberry GraphQL",
    "gqlgen": "gqlgen",
    "hasura": "Hasura",
    
    # Ruby on Rails
    "ruby on rails": "Ruby on Rails",
    
    # Serverless variants
    "aws lambda": "AWS Lambda",
    "firebase cloud functions": "Firebase Cloud Functions",
    "firebase functions": "Firebase Functions",
    "cloud functions for firebase": "Firebase Cloud Functions",
    "vercel serverless functions": "Vercel Serverless Functions",
    "netlify functions": "Netlify Functions",
    "serverless functions": "Serverless Functions",
    "serverless functions (faas)": "Serverless Functions",
    "supabase edge functions": "Supabase Edge Functions",
    
    # CMS/Headless CMS
    "strapi": "Strapi",
    "strapi (node.js)": "Strapi",
    "strapi (headless cms)": "Strapi",
    "strapi headless cms": "Strapi",
    
    # API Gateway variants
    "aws api gateway": "AWS API Gateway",
    "amazon api gateway": "AWS API Gateway",
    "api gateway": "API Gateway",
    "kong": "Kong",
    "kong api gateway": "Kong",
    "express gateway": "Express Gateway",
    "aws appsync (graphql)": "AWS AppSync",
    
    # Static Site Generators (when used as backend)
    "jekyll": "Jekyll",
    "eleventy (11ty)": "Eleventy",
    "eleventy": "Eleventy",
    
    # Other frameworks and tools
    "trpc": "tRPC",
    "hardhat": "Hardhat",
    "foundry": "Foundry",
    "celery": "Celery",
    "bull": "Bull",
    "bull queue library": "Bull",
    "multer": "Multer",
    "commander.js": "Commander.js",
    "http-proxy-middleware": "http-proxy-middleware",
    "gorilla/websocket": "Gorilla WebSocket",
    
    # Machine Learning/Data Science frameworks
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "tensorflow/pytorch": "TensorFlow/PyTorch",
    "python with tensorflow/pytorch": "TensorFlow/PyTorch",
    "scikit-learn": "Scikit-learn",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "dask": "Dask",
    "feast": "Feast",
    "aws sagemaker feature store": "AWS SageMaker Feature Store",
    "onnxruntime": "ONNX Runtime",
    "torchserve": "TorchServe",
    "tensorflow serving": "TensorFlow Serving",
    "nvidia triton inference server": "NVIDIA Triton",
    "amazon sagemaker": "Amazon SageMaker",
    "kubeflow": "Kubeflow",
    "seldon core": "Seldon Core",
    "pycaret": "PyCaret",
    "flink ml": "Flink ML",
    "tensorflow extended (tfx)": "TensorFlow Extended",
    
    # Streaming/Message Queue frameworks
    "apache kafka": "Apache Kafka",
    "kafka streams": "Kafka Streams",
    "amazon msk": "Amazon MSK",
    "aws kinesis data streams": "AWS Kinesis Data Streams",
    "aws kinesis data analytics": "AWS Kinesis Data Analytics",
    "aws kinesis data analytics (apache flink)": "AWS Kinesis + Flink",
    "apache flink": "Apache Flink",
    "flink": "Flink",
    "apache spark": "Apache Spark",
    "mllib": "MLlib",
    "apache airflow": "Apache Airflow",
    "apache nifi": "Apache NiFi",
    
    # Container/Orchestration (when used as backend)
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "amazon eks": "Amazon EKS",
    "istio": "Istio",
    "nginx ingress controller": "Nginx Ingress Controller",
    "envoy proxy": "Envoy Proxy",
    "etcd": "etcd",
    
    # Blockchain/P2P frameworks
    "libp2p": "libp2p",
    "js-libp2p": "js-libp2p",
    "the graph protocol": "The Graph Protocol",
    "openzeppelin contracts": "OpenZeppelin Contracts",
    "hyperledger fabric": "Hyperledger Fabric",
    "kademlia dht": "Kademlia DHT",
    "libp2p-webrtc-star": "libp2p-webrtc-star",
    "gossipsub": "GossipSub",
    
    # AI/NLP frameworks
    "rasa nlu": "Rasa NLU",
    "rasa core": "Rasa Core",
    "ray rllib": "Ray RLlib",
    "antlr": "ANTLR",
    "drools": "Drools",
    "mesa framework": "Mesa",
    
    # Other specialized frameworks
    "apache camel": "Apache Camel",
    "aws step functions": "AWS Step Functions",
    "aws iot core": "AWS IoT Core",
    "hashicorp terraform": "HashiCorp Terraform",
    "crdts/operational transforms": "CRDTs/OT",
    "go's standard library (net/http/httputil.reverseproxy)": "Go ReverseProxy",
    
    # Language specifications (when context is backend)
    "python": "Python",
    "java": "Java",
    "golang": "Go",
    "go": "Go",
    "go (golang)": "Go",
    "go (custom networking/audio stack)": "Go",
    "typescript": "TypeScript",
    "node.js": "Node.js",
    "node.js (with typescript)": "Node.js + TypeScript",
    "node.js (typescript)": "Node.js + TypeScript",
    
    # REST/HTTP specifications
    "restful apis": "REST API",
    "restful api": "REST API",
    "rest api": "REST API",
    "rest": "REST",
    "rest/http": "REST/HTTP",
    "websockets": "WebSockets",
    
    # None/No framework
    "none": "None",
    "none needed": "None",
    "none required": "None",
    "null": "None",
    
    # Add more backend framework synonyms as needed...
}

backend_languages_synonyms = {
    # Node.js variants
    "node.js": "Node.js",
    "nodejs": "Node.js",
    "node": "Node.js",
    "node.js with typescript": "Node.js + TypeScript",
    "node.js (with typescript)": "Node.js + TypeScript",
    "node.js (typescript)": "Node.js + TypeScript",
    "typescript (with node.js)": "Node.js + TypeScript",
    "typescript (node.js)": "Node.js + TypeScript",
    "node.js/typescript": "Node.js + TypeScript",
    "typescript with node.js": "Node.js + TypeScript",
    "node.js with express.js (using typescript)": "Node.js + TypeScript",
    "javascript (node.js)": "Node.js",
    
    # TypeScript variants
    "typescript": "TypeScript",
    "ts": "TypeScript",
    "typescript/deno": "TypeScript",
    
    # Python variants
    "python": "Python",
    "python 3": "Python",
    "python 3.x": "Python",
    "python 3.9+": "Python",
    "python 3.10+": "Python",
    "django (python)": "Python",
    
    # JavaScript variants
    "javascript": "JavaScript",
    "js": "JavaScript",
    "javascript/typescript": "JavaScript/TypeScript",
    "javascript (es6+)": "JavaScript",
    "vanilla javascript": "JavaScript",
    "vanilla javascript (es6+)": "JavaScript",
    
    # Go variants
    "go": "Go",
    "golang": "Go",
    "go (golang)": "Go",
    "golng": "Go",
    "go (or typescript/javascript)": "Go",
    
    # Java variants
    "java": "Java",
    "java 17+": "Java",
    "java/scala": "Java/Scala",
    "java (kotlin)": "Java + Kotlin",
    
    # Solidity variants
    "solidity": "Solidity",
    
    # Other languages
    "ruby": "Ruby",
    "rust": "Rust",
    "elixir": "Elixir",
    "kotlin": "Kotlin",
    "c++": "C++",
    "arduino ide (c++)": "C++",
    "scala": "Scala",
    "deno": "Deno",
    
    # HTML/CSS (when used as backend context)
    "html": "HTML",
    "html5": "HTML5",
    "css": "CSS",
    "html/css": "HTML/CSS",
    "vanilla html": "HTML",
    
    # AWS Lambda context
    "aws lambda (typescript, python, etc.)": "AWS Lambda Runtime",
    
    # Framework names (when used as language context)
    "django": "Python",
    
    # None/No language
    "none": "None",
    "none required": "None",
    "null": "None",
    
    # Add more backend language synonyms as needed...
}

authentication_synonyms = {
    # JWT variants
    "jwt": "JWT",
    "json web tokens (jwt)": "JWT",
    "json web tokens": "JWT",
    "jwt tokens": "JWT",
    "jwt (json web tokens)": "JWT",
    "jwt-based authentication": "JWT",
    "jwt-based": "JWT",
    "jwt-based auth": "JWT",
    "jwt-based system": "JWT",
    "jwt strategy": "JWT",
    "jwt sessions": "JWT",
    "jwt for authentication": "JWT",
    "jwts": "JWT",
    "jwts (json web tokens)": "JWT",
    "json web tokens (jwts)": "JWT",
    "jwt (json web token)": "JWT",
    "jwt-based authentication system": "JWT",
    "jwt-based custom authentication": "JWT",
    "jwt tokens with role-based access control": "JWT + RBAC",
    "jwt + role-based access control (rbac)": "JWT + RBAC",
    "jwts + rbac": "JWT + RBAC",
    "jwts (json web tokens) with rbac": "JWT + RBAC",
    "jwt (json web tokens) with role-based access control (rbac)": "JWT + RBAC",
    "jwt tokens with proper rbac implementation": "JWT + RBAC",
    "custom jwt": "JWT",
    "custom jwt-based authentication": "JWT",
    "custom jwt-based system": "JWT",
    "simple jwt": "JWT",
    "simple jwt (json web token) based authentication": "JWT",
    
    # JWT with specific libraries/frameworks
    "jsonwebtoken": "JWT + jsonwebtoken",
    "jsonwebtoken (jwts)": "JWT + jsonwebtoken",
    "jwt (json web tokens) with `bcrypt.js`": "JWT + bcrypt",
    "jwt (json web tokens) with `bcrypt`": "JWT + bcrypt",
    "jwt (json web tokens) with bcrypt": "JWT + bcrypt",
    "jwt (json web tokens) + bcrypt": "JWT + bcrypt",
    "jwt + bcrypt": "JWT + bcrypt",
    "json web tokens (jwt) + bcrypt": "JWT + bcrypt",
    "json web tokens (jwt) with bcrypt": "JWT + bcrypt",
    "jwt (json web tokens) with bcrypt for password hashing": "JWT + bcrypt",
    "jwt (json web tokens) with bcrypt hashing": "JWT + bcrypt",
    "jwt (json web tokens) with hashing": "JWT + bcrypt",
    "json web tokens (jwt) with hashed passwords": "JWT + bcrypt",
    "jwt (json web tokens) with `djangorestframework-simplejwt`": "JWT + DRF Simple JWT",
    "jwt (json web tokens) via `django-rest-framework-simplejwt`": "JWT + DRF Simple JWT",
    "jwt (json web tokens) via django rest framework simple jwt": "JWT + DRF Simple JWT",
    "jwt (json web tokens) with django rest framework simple jwt": "JWT + DRF Simple JWT",
    "jwt via djangorestframework-simplejwt": "JWT + DRF Simple JWT",
    "jwt (json web tokens) with drf simple jwt": "JWT + DRF Simple JWT",
    "django rest framework simple jwt": "DRF Simple JWT",
    "djangorestframework-simplejwt": "DRF Simple JWT",
    "django-rest-framework-simplejwt": "DRF Simple JWT",
    "drf simple jwt": "DRF Simple JWT",
    "django simple jwt": "DRF Simple JWT",
    "django's built-in auth + django rest framework simple jwt": "DRF Simple JWT",
    "django's built-in authentication + simple jwt": "DRF Simple JWT",
    "django's built-in user model + django rest framework simple jwt": "DRF Simple JWT",
    
    # JWT with refresh tokens
    "jwt (json web tokens) with refresh tokens": "JWT + Refresh Tokens",
    "jwt with refresh tokens": "JWT + Refresh Tokens",
    "json web tokens (jwts) with refresh tokens": "JWT + Refresh Tokens",
    "refresh tokens": "Refresh Tokens",
    
    # JWT with OAuth
    "jwt with oauth 2.0": "JWT + OAuth 2.0",
    "jwt (json web tokens) with oauth 2.0": "JWT + OAuth 2.0",
    "oauth 2.0 with jwt": "OAuth 2.0 + JWT",
    "oauth 2.0 with jwt tokens": "OAuth 2.0 + JWT",
    "oauth 2.0 with jwt (json web tokens)": "OAuth 2.0 + JWT",
    "oauth 2.0 + jwt": "OAuth 2.0 + JWT",
    "oauth 2.0 + jwt tokens": "OAuth 2.0 + JWT",
    "oauth 2.0 / jwt (json web tokens)": "OAuth 2.0 + JWT",
    "oauth 2.0 / jwt": "OAuth 2.0 + JWT",
    "json web tokens (jwt) with oauth 2.0": "JWT + OAuth 2.0",
    "jwt with oauth2.0": "JWT + OAuth 2.0",
    "jwt with oauth 2.0 integration": "JWT + OAuth 2.0",
    "oauth with jwt": "OAuth + JWT",
    
    # JWT with Passport.js
    "jwt (json web tokens) with passport.js": "JWT + Passport.js",
    "json web tokens (jwt) with passport.js": "JWT + Passport.js",
    "passport.js with jwt": "Passport.js + JWT",
    "passport.js (with jwt strategy)": "Passport.js + JWT",
    "passport.js with jwt (json web tokens)": "Passport.js + JWT",
    "passport.js (with jwt)": "Passport.js + JWT",
    "passport.js (with jwts)": "Passport.js + JWT",
    "passport.js with jwt tokens": "Passport.js + JWT",
    "passport.js with jwt strategy": "Passport.js + JWT",
    "jwt with passport.js": "JWT + Passport.js",
    "jwt + passport.js": "JWT + Passport.js",
    "json web tokens (jwt) & passport.js": "JWT + Passport.js",
    "jwt (json web tokens) & passport.js": "JWT + Passport.js",
    "jwt (json web tokens) + passport.js": "JWT + Passport.js",
    "jwt (json web tokens) + passport.js + bcrypt": "JWT + Passport.js + bcrypt",
    "passport.js (with jwts) & bcrypt": "Passport.js + JWT + bcrypt",
    "jwt (json web tokens) with passport.js and bcrypt": "JWT + Passport.js + bcrypt",
    "passport.js combined with jwt (json web tokens)": "Passport.js + JWT",
    "jwts (json web tokens) with passport.js": "JWT + Passport.js",
    "passport.js/jwt": "Passport.js + JWT",
    
    # JWT with specific frameworks
    "jwt (json web tokens) with fastapi": "JWT + FastAPI",
    "jwt (json web tokens) with django's user system": "JWT + Django",
    "jwt (json web tokens) with django": "JWT + Django",
    "jwts (json web tokens) with django's built-in auth": "JWT + Django",
    "django's built-in authentication system supplemented with jwt (json web tokens)": "JWT + Django",
    "jwt (json web tokens) + passport.js (with nestjs)": "JWT + Passport.js + NestJS",
    "passport.js (integrated with nestjs)": "Passport.js + NestJS",
    "passport.js (integrated into nestjs)": "Passport.js + NestJS",
    "passport.js (with nestjs `@nestjs/passport` module)": "Passport.js + NestJS",
    "passport.js (within nestjs) with jwt (json web tokens)": "Passport.js + JWT + NestJS",
    "jwt (json web tokens) with passport.js (integrated with nestjs)": "JWT + Passport.js + NestJS",
    
    # JWT with cookies
    "jwt (json web tokens) with httponly cookies": "JWT + HTTP-Only Cookies",
    "jwt (json web tokens) with http-only cookies": "JWT + HTTP-Only Cookies",
    "http-only cookies": "HTTP-Only Cookies",
    "jwt with local storage": "JWT + Local Storage",
    "simple jwt with local storage": "JWT + Local Storage",
    
    # Auth0 variants
    "auth0": "Auth0",
    "auth0 service": "Auth0",
    "auth0 (saas identity platform)": "Auth0",
    "auth0 (saas)": "Auth0",
    "auth0 with jwt": "Auth0 + JWT",
    "auth0 with jwt tokens": "Auth0 + JWT",
    "jwt tokens with auth0 integration": "Auth0 + JWT",
    "auth0 with role-based access control": "Auth0 + RBAC",
    "auth0 with multi-factor authentication": "Auth0 + MFA",
    "oauth 2.0 with auth0": "Auth0 + OAuth 2.0",
    "oauth 2.0 (using auth0)": "Auth0 + OAuth 2.0",
    "oauth 2.0 implemented through auth0": "Auth0 + OAuth 2.0",
    "oauth 2.0 using auth0": "Auth0 + OAuth 2.0",
    "oauth2.0 with auth0": "Auth0 + OAuth 2.0",
    "oauth2 with auth0": "Auth0 + OAuth 2.0",
    "auth0 or firebase authentication": "Auth0/Firebase",
    "auth0 / okta": "Auth0/Okta",
    "auth0 / okta / aws cognito / google identity platform": "Auth0/Okta/Cognito",
    "auth0, okta, keycloak, or even google/github": "Auth0/Okta/Keycloak",
    
    # Firebase Authentication variants
    "firebase authentication": "Firebase Authentication",
    "firebase auth": "Firebase Authentication",
    "firebase authentication (email/password)": "Firebase Authentication",
    "firebase authentication with jwt": "Firebase Authentication + JWT",
    "firebase authentication (email/password and google sign-in)": "Firebase Authentication",
    "firebase authentication with google oauth support": "Firebase Authentication + Google",
    "firebase authentication (with google oauth support)": "Firebase Authentication + Google",
    "firebase authentication with metamask": "Firebase Authentication + MetaMask",
    "firebase authentication (anonymous auth)": "Firebase Authentication",
    
    # OAuth variants
    "oauth": "OAuth",
    "oauth 2.0": "OAuth 2.0",
    "oauth2": "OAuth 2.0",
    "oauth2.0": "OAuth 2.0",
    "oauth 2.0/openid connect": "OAuth 2.0 + OpenID Connect",
    "oauth 2.0 / openid connect": "OAuth 2.0 + OpenID Connect",
    "oauth 2.0 with openid connect": "OAuth 2.0 + OpenID Connect",
    "oauth 2.0 and openid connect": "OAuth 2.0 + OpenID Connect",
    "oauth 2.0/oidc": "OAuth 2.0 + OIDC",
    "oauth2/oidc": "OAuth 2.0 + OIDC",
    "oauth2/openid connect": "OAuth 2.0 + OpenID Connect",
    "oauth2.0/openid connect": "OAuth 2.0 + OpenID Connect",
    "oauth 2.0 / openid connect (oidc)": "OAuth 2.0 + OIDC",
    "oauth 2.0 / openid connect flows": "OAuth 2.0 + OpenID Connect",
    "oauth 2.0 with jwt and passport.js": "OAuth 2.0 + JWT + Passport.js",
    "oauth integration": "OAuth",
    "oauth integration with github": "OAuth + GitHub",
    "oauth integration with orcid": "OAuth + ORCID",
    "oauth with github": "OAuth + GitHub",
    "oauth 2.0 via github": "OAuth 2.0 + GitHub",
    "github oauth": "GitHub OAuth",
    "google oauth": "Google OAuth",
    "oauth 2.0 with providers like google, github": "OAuth 2.0 + Providers",
    "oauth 2.0 flow": "OAuth 2.0",
    "oauth2 flow": "OAuth 2.0",
    "oauth 2.0 implementation with pkce": "OAuth 2.0 + PKCE",
    
    # Passport.js variants
    "passport.js": "Passport.js",
    "passport.js (local strategy)": "Passport.js Local",
    "passport.js (local strategy with bcrypt)": "Passport.js Local + bcrypt",
    "passport.js (local strategy) + express-session + bcrypt": "Passport.js Local + Session + bcrypt",
    "passport.js (with local strategy)": "Passport.js Local",
    "passport.js (for oauth)": "Passport.js OAuth",
    "passport.js (oauth 2.0)": "Passport.js OAuth 2.0",
    "passport-jwt": "passport-jwt",
    
    # NextAuth.js variants
    "nextauth.js": "NextAuth.js",
    "nextauth.js with jwt": "NextAuth.js + JWT",
    "nextauth.js + jwt (json web tokens)": "NextAuth.js + JWT",
    "nextauth.js (now auth.js)": "NextAuth.js",
    "nextauth.js (auth.js)": "NextAuth.js",
    "auth.js": "Auth.js",
    "auth.js (formerly nextauth.js)": "Auth.js",
    "nextauth.js with google provider": "NextAuth.js + Google",
    "nextauth.js (frontend)": "NextAuth.js",
    "nextauth.js (for next.js frontend) & jwts (for backend api)": "NextAuth.js + JWT",
    "nextauth.js (frontend) + jwt (backend)": "NextAuth.js + JWT",
    
    # AWS Cognito variants
    "aws cognito": "AWS Cognito",
    "amazon cognito": "AWS Cognito",
    "aws cognito user pools": "AWS Cognito User Pools",
    "amazon cognito user pools": "AWS Cognito User Pools",
    "aws cognito (user pools)": "AWS Cognito User Pools",
    "amazon cognito identity pools": "AWS Cognito Identity Pools",
    "aws cognito + custom roles": "AWS Cognito + RBAC",
    "aws cognito + jwt": "AWS Cognito + JWT",
    "jwt (json web tokens) with aws cognito": "AWS Cognito + JWT",
    "jwts with aws cognito": "AWS Cognito + JWT",
    "oauth 2.0 with aws cognito": "AWS Cognito + OAuth 2.0",
    "aws cognito + oauth 2.0 / openid connect": "AWS Cognito + OAuth 2.0 + OIDC",
    "aws cognito with multi-factor authentication": "AWS Cognito + MFA",
    
    # Clerk variants
    "clerk": "Clerk",
    "clerk.dev": "Clerk",
    
    # Supabase Auth variants
    "supabase": "Supabase Auth",
    "supabase auth": "Supabase Auth",
    
    # Okta variants
    "okta": "Okta",
    "oauth 2.0 with okta": "Okta + OAuth 2.0",
    
    # Keycloak variants
    "keycloak": "Keycloak",
    "keycloak (self-hosted)": "Keycloak",
    "keycloak (openid connect / oauth 2.0 provider)": "Keycloak + OIDC",
    "keycloak with oauth 2.0/openid connect": "Keycloak + OAuth 2.0 + OIDC",
    "oauth 2.0 with keycloak": "Keycloak + OAuth 2.0",
    
    # OpenID Connect variants
    "openid connect": "OpenID Connect",
    "oidc": "OpenID Connect",
    "openid connect (oidc)": "OpenID Connect",
    "oidc (openid connect)": "OpenID Connect",
    "openid connect (oidc) / oauth2": "OpenID Connect + OAuth 2.0",
    "openid connect (oidc) + did-based key signing": "OpenID Connect + DID",
    "openid connect with mfa support": "OpenID Connect + MFA",
    "oidc/oauth2": "OIDC + OAuth 2.0",
    "oidc (openid connect)": "OpenID Connect",
    
    # bcrypt variants
    "bcrypt": "bcrypt",
    "bcrypt.js": "bcrypt.js",
    "bcryptjs": "bcrypt.js",
    "bcrypt.js": "bcrypt.js",
    "`bcrypt`": "bcrypt",
    "json web tokens (jwt) & bcrypt": "JWT + bcrypt",
    
    # Django authentication variants
    "django's built-in authentication system": "Django Authentication",
    "django's built-in authentication": "Django Authentication",
    "django's built-in auth system": "Django Authentication",
    "django's built-in auth": "Django Authentication",
    "django's built-in": "Django Authentication",
    "django's built-in user system": "Django Authentication",
    "django's built-in user model": "Django Authentication",
    "django's built-in user model & authentication system": "Django Authentication",
    "django's built-in user model and authentication system": "Django Authentication",
    "django's built-in user authentication system": "Django Authentication",
    "django's built-in session-based authentication": "Django Session Authentication",
    "django's built-in session authentication": "Django Session Authentication",
    "django's session-based authentication": "Django Session Authentication",
    "django's built-in admin": "Django Admin",
    "django's built-in admin panel": "Django Admin",
    "django's built-in admin authentication": "Django Admin",
    "django admin authentication": "Django Admin",
    "django user and group models": "Django User Model",
    "django's user model": "Django User Model",
    "django.contrib.auth": "Django Authentication",
    "django's built-in `django.contrib.auth`": "Django Authentication",
    "django's built-in `auth` system + drf token/jwt authentication": "Django Authentication + DRF",
    "django's built-in user system with drf token authentication": "Django Authentication + DRF Token",
    "django's built-in auth system + drf token authentication": "Django Authentication + DRF Token",
    "django's built-in auth + drf token authentication": "Django Authentication + DRF Token",
    "django's built-in user system + drf token authentication": "Django Authentication + DRF Token",
    "django's built-in auth system + custom rbac implementation": "Django Authentication + RBAC",
    
    # DRF Token Authentication
    "django rest framework's token authentication": "DRF Token Authentication",
    "django rest framework's session authentication": "DRF Session Authentication",
    "drf token": "DRF Token Authentication",
    "drf token auth": "DRF Token Authentication",
    "drf token authentication": "DRF Token Authentication",
    "drf's token authentication": "DRF Token Authentication",
    "django rest framework token authentication": "DRF Token Authentication",
    "token authentication": "Token Authentication",
    "token-based authentication": "Token Authentication",
    
    # Flask authentication variants
    "flask-login": "Flask-Login",
    "flask-login + bcrypt": "Flask-Login + bcrypt",
    "flask-jwt-extended": "Flask-JWT-Extended",
    "session-based (flask-login)": "Flask-Login",
    
    # Web3/Blockchain authentication
    "metamask": "MetaMask",
    "metamask integration": "MetaMask",
    "metamask/walletconnect": "MetaMask/WalletConnect",
    "walletconnect": "WalletConnect",
    "wallet connect": "WalletConnect",
    "walletconnect 2.0": "WalletConnect 2.0",
    "walletconnect and metamask": "WalletConnect + MetaMask",
    "walletconnect and metamask integration": "WalletConnect + MetaMask",
    "web3 wallet authentication": "Web3 Wallet Authentication",
    "web3 auth": "Web3 Authentication",
    "web3 authentication": "Web3 Authentication",
    "web3 wallet connect": "Web3 Wallet Connect",
    "web3 wallet connection": "Web3 Wallet Connection",
    "web3 wallet (e.g., metamask, walletconnect)": "Web3 Wallet",
    "web3 wallets": "Web3 Wallets",
    "web3 wallets (e.g., metamask)": "Web3 Wallets",
    "ethereum wallets": "Ethereum Wallets",
    "ethereum wallets (e.g., metamask)": "Ethereum Wallets",
    "ethereum wallet authentication": "Ethereum Wallet Authentication",
    "ethereum wallet-based authentication": "Ethereum Wallet Authentication",
    "ethereum wallet-based authentication using metamask": "Ethereum Wallet Authentication + MetaMask",
    "ethereum wallet-based authentication (sign-in with ethereum)": "Ethereum Wallet Authentication + SIWE",
    "wallet-based authentication": "Wallet-Based Authentication",
    "wallet-based": "Wallet-Based Authentication",
    "wallet-based (web3)": "Web3 Wallet Authentication",
    "wallet-based authentication (sign-in with ethereum)": "Wallet-Based Authentication + SIWE",
    "wallet-based authentication (web3 auth)": "Web3 Wallet Authentication",
    "wallet-based (e.g., metamask, walletconnect)": "Wallet-Based Authentication",
    "wallet-based authentication & token-gating": "Wallet-Based Authentication + Token Gating",
    "wallet-based login using metamask": "MetaMask Login",
    "wallet-based authentication (e.g., sign-in with ethereum - siwe)": "Wallet-Based Authentication + SIWE",
    "wallet-based (sign-in with ethereum)": "Wallet-Based Authentication + SIWE",
    "wallet-based (via wagmi/web3modal)": "Wallet-Based Authentication + Wagmi",
    "web3 wallet (e.g., metamask, walletconnect)": "Web3 Wallet",
    "web3 wallet-based authentication": "Web3 Wallet Authentication",
    "web3 wallet-based authentication (metamask, walletconnect)": "Web3 Wallet Authentication",
    "web3 wallet (signature-based)": "Web3 Wallet Signature",
    "wallet signatures": "Wallet Signatures",
    "cryptocurrency wallet authentication": "Crypto Wallet Authentication",
    "cryptocurrency wallet connection": "Crypto Wallet Connection",
    "message signing": "Message Signing",
    "signature verification": "Signature Verification",
    "connect with metamask/walletconnect": "MetaMask/WalletConnect",
    "web3modal": "Web3Modal",
    "web3-modal": "Web3Modal",
    
    # Sign-in with Ethereum (SIWE)
    "siwe": "SIWE",
    "sign-in with ethereum (siwe)": "SIWE",
    "sign-in with ethereum": "SIWE",
    "sign-in with ethereum (eip-4361)": "SIWE",
    "eip-4361 (sign-in with ethereum - siwe)": "SIWE",
    "eip-4361: sign-in with ethereum": "SIWE",
    "eip-4361 (sign-in with ethereum)": "SIWE",
    "eip-4361 (sign-in with ethereum - siwe)": "SIWE",
    "sign-in with ethereum (siwe) protocol": "SIWE",
    "sign-in with ethereum (siwe) + jwts": "SIWE + JWT",
    "sign-in with ethereum (sive)": "SIWE",
    "sign-in with ethereum (eip-4361 / siwe)": "SIWE",
    "walletconnect + eip-4361 (sign-in with ethereum)": "WalletConnect + SIWE",
    "walletconnect + sign-in with ethereum (siwe - eip-4361)": "WalletConnect + SIWE",
    "ens (ethereum name service) + sign-in with ethereum": "ENS + SIWE",
    "decentralized authentication with web3.js": "Web3.js Authentication",
    
    # Decentralized Identity
    "ceramic network": "Ceramic Network",
    "ceramic network with did": "Ceramic Network + DID",
    "ceramic network (with did-based profiles)": "Ceramic Network + DID",
    "ceramic network with idx": "Ceramic Network + IDX",
    "self-sovereign identity using ceramic network and idx": "Ceramic Network + IDX",
    "idx": "IDX",
    "3id connect": "3ID Connect",
    "polygon id": "Polygon ID",
    "uport": "uPort",
    "civic": "Civic",
    "passbase": "Passbase",
    "persona": "Persona",
    "onfido": "Onfido",
    "proof of humanity": "Proof of Humanity",
    "worldcoin": "Worldcoin",
    "decentralized identifiers (dids)": "DIDs",
    "dids": "DIDs",
    "dids (decentralized identifiers)": "DIDs",
    "w3c decentralized identifiers (dids)": "DIDs",
    "did:ethr": "DID:ethr",
    "decentralized ids": "DIDs",
    "self-sovereign identity": "Self-Sovereign Identity",
    "self-sovereign identity using hyperledger indy": "Hyperledger Indy SSI",
    "sovrin": "Sovrin",
    "hyperledger indy": "Hyperledger Indy",
    "verifiable credentials": "Verifiable Credentials",
    "erc-725": "ERC-725",
    "erc-735": "ERC-735",
    "zero-knowledge proofs": "Zero-Knowledge Proofs",
    "zero-knowledge proofs (zk-snarks)": "zk-SNARKs",
    "zkp": "Zero-Knowledge Proofs",
    
    # Multi-Factor Authentication
    "multi-factor authentication": "MFA",
    "mfa": "MFA",
    "totp": "TOTP",
    "totp (time-based one-time password)": "TOTP",
    "time-based otp": "TOTP",
    "twilio authy": "Twilio Authy",
    "authy": "Authy",
    "google authenticator": "Google Authenticator",
    "fido2 / webauthn": "FIDO2/WebAuthn",
    "webauthn api": "WebAuthn API",
    "webauthn/fido2": "WebAuthn/FIDO2",
    "standard email/password with mfa": "Email/Password + MFA",
    
    # Role-Based Access Control
    "rbac": "RBAC",
    "role-based access control (rbac)": "RBAC",
    "role-based access control": "RBAC",
    "custom rbac implementation": "Custom RBAC",
    "custom rbac": "Custom RBAC",
    "custom rbac system": "Custom RBAC",
    "role-based access control (rbac) implemented in fastapi backend": "RBAC + FastAPI",
    "role-based access control (rbac) implemented in your fastapi backend": "RBAC + FastAPI",
    "abac": "ABAC",
    "attribute-based access control (abac)": "ABAC",
    
    # Session-based Authentication
    "session-based authentication": "Session Authentication",
    "basic session-based authentication": "Session Authentication",
    "simple session-based authentication": "Session Authentication",
    "simple session-based": "Session Authentication",
    "session authentication": "Session Authentication",
    "session management": "Session Management",
    "backend-managed sessions/jwts": "Session/JWT Management",
    
    # API Key Authentication
    "api key authentication": "API Key Authentication",
    "api key": "API Key",
    "api keys": "API Keys",
    "api key-based access control": "API Key Access Control",
    "api key based": "API Key Authentication",
    "simple api key": "API Key",
    "simple api key / bearer token": "API Key/Bearer Token",
    "custom api key management": "Custom API Key Management",
    "basic api key / hardcoded user credential": "API Key/Hardcoded",
    "shared secret api key": "Shared Secret API Key",
    "shared secrets": "Shared Secrets",
    
    # Basic Authentication
    "basic auth": "Basic Authentication",
    "basic http authentication": "Basic HTTP Authentication",
    "http basic authentication": "Basic HTTP Authentication",
    "basic authentication with express middleware": "Basic Authentication + Express",
    "express-basic-auth": "express-basic-auth",
    "basic email validation": "Email Validation",
    "email validation": "Email Validation",
    "email verification": "Email Verification",
    "email/password": "Email/Password",
    "email/password authentication": "Email/Password",
    "email/password with jwt": "Email/Password + JWT",
    "jwt (json web tokens) with email/password": "Email/Password + JWT",
    "jwt (json web tokens) (jwt) with email/password": "Email/Password + JWT",
    
    # HTTPS/TLS/SSL
    "https": "HTTPS",
    "https/ssl": "HTTPS/SSL",
    "https/tls": "HTTPS/TLS",
    "tls": "TLS",
    "tls/ssl": "TLS/SSL",
    "ssl/tls": "SSL/TLS",
    "https/ssl certificates": "HTTPS/SSL Certificates",
    "https with tls 1.3": "HTTPS + TLS 1.3",
    "let's encrypt": "Let's Encrypt",
    "certificate-based authentication": "Certificate Authentication",
    "x.509 certificates": "X.509 Certificates",
    "mutual tls (mtls)": "Mutual TLS",
    
    # SAML
    "saml": "SAML",
    "saml federation": "SAML Federation",
    "saml/oidc": "SAML/OIDC",
    
    # AWS IAM
    "aws iam": "AWS IAM",
    "aws iam (identity and access management)": "AWS IAM",
    "aws iam identity center": "AWS IAM Identity Center",
    "aws iam roles": "AWS IAM Roles",
    "iam": "IAM",
    
    # Hashing/Encryption
    "argon2": "Argon2",
    "passlib": "passlib",
    "pyjwt": "PyJWT",
    "python-jose": "python-jose",
    "aes-256": "AES-256",
    "hmac-sha256": "HMAC-SHA256",
    "hmac sha-256 signatures": "HMAC-SHA256",
    "hmac signatures": "HMAC Signatures",
    "hmac signature verification": "HMAC Signature Verification",
    "kms": "KMS",
    "aws kms": "AWS KMS",
    "aws secrets manager": "AWS Secrets Manager",
    "hashicorp vault": "HashiCorp Vault",
    "vault by hashicorp": "HashiCorp Vault",
    "werkzeug.security": "Werkzeug Security",
    "werkzeug security utilities": "Werkzeug Security",
    
    # FastAPI-specific
    "fastapi-users": "FastAPI-Users",
    "fastapi's built-in oauth2 with bearer tokens (jwts)": "FastAPI OAuth2 + JWT",
    
    # Social Login Providers
    "google": "Google OAuth",
    "google sign-in": "Google Sign-In",
    "google sso": "Google SSO",
    "twitter": "Twitter OAuth",
    "github": "GitHub OAuth",
    "github authentication": "GitHub Authentication",
    "github integration": "GitHub Integration",
    "github sso": "GitHub SSO",
    "gitlab": "GitLab OAuth",
    "gitlab sso": "GitLab SSO",
    "facebook": "Facebook OAuth",
    "apple": "Apple OAuth",
    "social logins": "Social Logins",
    
    # CMS-specific Authentication
    "strapi's built-in authentication system": "Strapi Authentication",
    "strapi's built-in admin authentication": "Strapi Admin Authentication",
    "strapi's built-in admin panel authentication": "Strapi Admin Authentication",
    "strapi's built-in users & permissions": "Strapi Users & Permissions",
    "sanity's built-in auth": "Sanity Authentication",
    "sanity.io's built-in auth": "Sanity Authentication",
    "sanity's built-in authentication system": "Sanity Authentication",
    "sanity.io built-in authentication": "Sanity Authentication",
    "contentful's built-in user management": "Contentful User Management",
    "contentful's built-in authentication": "Contentful Authentication",
    
    # Policy Engines
    "opa (open policy agent)": "Open Policy Agent",
    "open policy agent (opa)": "Open Policy Agent",
    "open policy agent": "Open Policy Agent",
    
    # Rate Limiting/Security
    "express-rate-limit": "Express Rate Limit",
    "api rate limiting": "API Rate Limiting",
    "captcha": "CAPTCHA",
    "google recaptcha": "Google reCAPTCHA",
    "aws waf": "AWS WAF",
    "api gateway authorizers": "API Gateway Authorizers",
    "ip whitelisting": "IP Whitelisting",
    "helmet.js": "Helmet.js",
    
    # Enterprise/Directory Services
    "ldap": "LDAP",
    "azure active directory": "Azure Active Directory",
    
    # Blockchain-specific
    "hyperledger fabric ca (certificate authority)": "Hyperledger Fabric CA",
    "hyperledger fabric ca": "Hyperledger Fabric CA",
    "hyperledger fabric's certificate authority (ca)": "Hyperledger Fabric CA",
    "membership service provider (msp)": "MSP",
    "public key infrastructure (pki)": "PKI",
    "public/private key pairs": "Public/Private Key Pairs",
    "cryptographic key pairs (ed25519)": "Ed25519 Key Pairs",
    "trust on first use (tofu)": "TOFU",
    "hierarchical deterministic wallets (hd wallets)": "HD Wallets",
    "blockchain wallets": "Blockchain Wallets",
    "ethereum": "Ethereum",
    "polygon": "Polygon",
    "ethereum mainnet": "Ethereum Mainnet",
    "ens (ethereum name service)": "ENS",
    "ens (ethereum name service) integration": "ENS Integration",
    
    # Middleware/Libraries
    "express-jwt middleware": "express-jwt",
    "authlib": "Authlib",
    "django-allauth": "django-allauth",
    "devise": "Devise",
    
    # Spring Security
    "spring security": "Spring Security",
    "spring security (with jwts)": "Spring Security + JWT",
    
    # Other/Miscellaneous
    "access token": "Access Token",
    "refresh tokens": "Refresh Tokens",
    "qr code verification": "QR Code Verification",
    "signal protocol-style key verification": "Signal Protocol Verification",
    "simple passcode verification": "Passcode Verification",
    "simple password protection": "Password Protection",
    "simple password-based auth": "Password Authentication",
    "simple password-based auth with jwt tokens": "Password + JWT",
    "simple server-side password check": "Server-Side Password Check",
    "basic site-wide password": "Site-Wide Password",
    "locally stored master password": "Local Master Password",
    "master passphrase": "Master Passphrase",
    "simple admin password": "Admin Password",
    "simple \"admin link\" generated alongside share link": "Admin Link",
    "dkim": "DKIM",
    "spf": "SPF",
    "orcid": "ORCID",
    "orcid oauth": "ORCID OAuth",
    "orcid oauth2": "ORCID OAuth2",
    "service account": "Service Account",
    "http authentication": "HTTP Authentication",
    "environment variables": "Environment Variables",
    "basic environment variables": "Environment Variables",
    "custom middleware with jwt": "Custom JWT Middleware",
    "jwt (json web tokens) with custom middleware": "Custom JWT Middleware",
    "custom implementation using jwt tokens": "Custom JWT Implementation",
    "jwt tokens, https, and proper data validation": "JWT + HTTPS + Validation",
    "jwt tokens, rate limiting, and input validation": "JWT + Rate Limiting + Validation",
    "jwt tokens with auth0 integration": "JWT + Auth0",
    "custom django permissions": "Custom Django Permissions",
    "view decorators": "View Decorators",
    "aws api gateway integrated with aws iam": "AWS API Gateway + IAM",
    "aws iot core": "AWS IoT Core",
    "aws iot policies": "AWS IoT Policies",
    "metamask (via ethers.js)": "MetaMask + Ethers.js",
    "oauth 2.0 with metamask": "OAuth 2.0 + MetaMask",
    
    # None/Not Required variants
    "none": "None",
    "null": "None",
    "none required": "None",
    "none needed": "None",
    "not needed": "None",
    "not necessary": "None",
    "not required": "None",
    "not applicable": "None",
    "not applicable for a basic static site": "None",
    "no authentication": "None",
    "no authentication needed": "None",
    "no authentication required": "None",
    "no authentication is required": "None",
    "no authentication is needed initially": "None",
    "no user authentication is required": "None",
    "no user accounts": "None",
    "no account creation required": "None",
    "none for public viewing": "None",
    "none (for users)": "None",
    "none (for public browsing. if an admin panel for content management is added later, implement simple user/password with jwts": "None",
    "none (as per requirements)": "None",
    "not required for this project as specified": "None",
    "not needed for this project": "None",
    "not needed for mvp": "None",
    "not required for core functionality": "None",
    "not required for basic functionality": "None",
    "not required for initial version": "None",
    "not required initially": "None",
    "no authentication initially": "None",
    "none needed for this project's scope": "None",
    "none for the basic converter": "None",
    "none required (just email validation)": "None",
    "not applicable - core requirement is email uniqueness validation, not full user authentication": "None",
    "basic email validation (no user accounts needed)": "None",
    "not applicable": "None",
    "not needed": "None",
    "n/a": "None",
    "n/a (none)": "None",
    "not applicable": "None",
    "none": "None",
    
    # Add more authentication synonyms as needed...
}

# Dictionary mapping synonyms to their canonical/preferred names, organized by category
TECH_SYNONYMS = {
    'hosting': hosting_synonyms,
    
    'frontend_frameworks': frontend_frameworks_synonyms,
    
    'frontend_styling_solutions': frontend_styling_synonyms,
    
    'frontend_libraries': frontend_libraries_synonyms,
    
    'backend_frameworks': backend_frameworks_synonyms,
    
    'backend_languages': backend_languages_synonyms,
    
    'authentication': authentication_synonyms,
    
    'orms': {
        "sequelize": "Sequelize",
        "mongoose": "Mongoose",
        "prisma": "Prisma",
        "typeorm": "TypeORM",
        # Add more ORM synonyms as needed...
    },
    
    'databases': {
        "mongodb": "MongoDB",
        "mongo": "MongoDB",
        "postgresql": "PostgreSQL",
        "postgres": "PostgreSQL",
        "mysql": "MySQL",
        "sqlite": "SQLite",
        "redis": "Redis",
        # Add more database synonyms as needed...
    },
    
    'other_tools': {
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "k8s": "Kubernetes",
        "git": "Git",
        "github": "GitHub",
        "gitlab": "GitLab",
        # Add more tools synonyms as needed...
    }
}

# Create comprehensive ORMs synonyms dictionary
orms_synonyms = {
    # Mongoose variants
    "mongoose": "Mongoose",
    "mongoose odm": "Mongoose",
    "mongoose.js": "Mongoose",
    "mongoose (odm)": "Mongoose",
    "mongoose odm (object data modeling)": "Mongoose",
    "mongoose orm": "Mongoose",
    
    # Sequelize variants
    "sequelize": "Sequelize",
    "sequelize orm": "Sequelize",
    "sequelize (orm)": "Sequelize",
    "sequelize.js": "Sequelize",
    "sequelize/typeorm": "Sequelize",
    
    # Prisma variants
    "prisma": "Prisma",
    "prisma.js": "Prisma",
    "prisma.io": "Prisma",
    "prisma orm": "Prisma",
    "prisma (for node.js)": "Prisma",
    
    # TypeORM variants
    "typeorm": "TypeORM",
    "typeorm / prisma": "TypeORM",
    "pg-typeorm": "TypeORM",
    
    # SQLAlchemy variants
    "sqlalchemy": "SQLAlchemy",
    "sqlalchemy orm": "SQLAlchemy",
    "sqlalchemy 2.0": "SQLAlchemy 2.0",
    "sqlalchemy 2.0+": "SQLAlchemy 2.0+",
    "sqlalchemy 2.0+ (async)": "SQLAlchemy 2.0+",
    "sqlalchemy 2.0 with alembic": "SQLAlchemy 2.0",
    "sqlalchemy (with alembic for migrations)": "SQLAlchemy",
    "sqlalchemy (with flask-sqlalchemy)": "SQLAlchemy",
    "sqlalchemy (asyncpg dialect for postgresql)": "SQLAlchemy",
    "sqlalchemy/alembic": "SQLAlchemy",
    "sqlalchemy core": "SQLAlchemy Core",
    
    # Django ORM variants
    "django's orm": "Django ORM",
    "django orm": "Django ORM",
    "django's built-in orm": "Django ORM",
    "django": "Django ORM",
    "django's built-in permissions system": "Django ORM",
    "django's native permission system (rbac)": "Django ORM",
    
    # GORM variants
    "gorm": "GORM",
    
    # Knex.js variants
    "knex.js": "Knex.js",
    "knex": "Knex.js",
    "knex.js with objection.js": "Knex.js + Objection.js",
    
    # Flask-SQLAlchemy variants
    "flask-sqlalchemy": "Flask-SQLAlchemy",
    
    # Objection.js variants
    "objection.js": "Objection.js",
    
    # SQLModel variants
    "sqlmodel": "SQLModel",
    
    # Alembic variants
    "alembic": "Alembic",
    
    # Flask-Migrate variants
    "flask-migrate": "Flask-Migrate",
    
    # asyncpg variants
    "asyncpg": "asyncpg",
    
    # Spring Data JPA variants
    "spring data jpa": "Spring Data JPA",
    "jpa/hibernate": "JPA/Hibernate",
    
    # pg variants
    "pg": "pg",
    "pg-promise": "pg-promise",
    
    # database/sql variants
    "database/sql": "database/sql",
    "github.com/mattn/go-sqlite3": "go-sqlite3",
    
    # sqlx variants
    "sqlx": "sqlx",
    
    # Pydantic variants
    "pydantic": "Pydantic",
    
    # GeoAlchemy2 variants
    "geoalchemy2": "GeoAlchemy2",
    
    # Drizzle ORM variants
    "drizzle orm": "Drizzle ORM",
    
    # Generic ORM variants
    "object-relational mapper (orm)": "ORM",
    "orm": "ORM",
    
    # None/No ORM variants
    "none": "None",
    "null": "None",
    "none required": "None",
    "none": "None",
    "no database required": "None",
    "none on server side": "None",
    
    # Add more ORM synonyms as needed...
}

# Update TECH_SYNONYMS to use the new orms_synonyms dictionary
TECH_SYNONYMS = {
    'hosting': hosting_synonyms,
    
    'frontend_frameworks': frontend_frameworks_synonyms,
    
    'frontend_styling_solutions': frontend_styling_synonyms,
    
    'frontend_libraries': frontend_libraries_synonyms,
    
    'backend_frameworks': backend_frameworks_synonyms,
    
    'backend_languages': backend_languages_synonyms,
    
    'authentication': authentication_synonyms,
    
    'orms': orms_synonyms,
    
    'databases': {
        "mongodb": "MongoDB",
        "mongo": "MongoDB",
        "postgresql": "PostgreSQL",
        "postgres": "PostgreSQL",
        "mysql": "MySQL",
        "sqlite": "SQLite",
        "redis": "Redis",
        # Add more database synonyms as needed...
    },
    
    'other_tools': {
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "k8s": "Kubernetes",
        "git": "Git",
        "github": "GitHub",
        "gitlab": "GitLab",
        # Add more tools synonyms as needed...
    }
}

# Create comprehensive databases synonyms dictionary
databases_synonyms = {
    # MongoDB variants
    "mongodb": "MongoDB",
    "mongo": "MongoDB",
    "mongodb atlas": "MongoDB Atlas",
    "mongodb (nosql)": "MongoDB",
    "nosql (mongodb)": "MongoDB",
    "mongodb (nosql document database)": "MongoDB",
    "mongodb (via atlas)": "MongoDB Atlas",
    "mongodb (via mongodb atlas)": "MongoDB Atlas",
    "mongodb (using atlas)": "MongoDB Atlas",
    "atlas mongodb": "MongoDB Atlas",
    "mongodb atlas search": "MongoDB Atlas",
    "mongodb time-series collections": "MongoDB",
    "amazon documentdb (mongodb compatibility)": "Amazon DocumentDB",
    
    # PostgreSQL variants
    "postgresql": "PostgreSQL",
    "postgres": "PostgreSQL",
    "postgresql (postgres)": "PostgreSQL",
    "postgresql (aws rds for postgresql)": "AWS RDS PostgreSQL",
    "postgresql (aws rds postgresql)": "AWS RDS PostgreSQL",
    "postgresql (via aws rds)": "AWS RDS PostgreSQL",
    "postgresql (via aws rds for postgresql)": "AWS RDS PostgreSQL",
    "postgresql (managed by aws rds)": "AWS RDS PostgreSQL",
    "postgresql (managed via aws rds aurora postgresql)": "AWS Aurora PostgreSQL",
    "postgresql (managed by supabase)": "Supabase PostgreSQL",
    "postgresql (via supabase)": "Supabase PostgreSQL",
    "postgresql (production)": "PostgreSQL",
    "postgresql 15.x+": "PostgreSQL",
    "postgresql (with jsonb)": "PostgreSQL",
    "postgresql (with jsonb data type)": "PostgreSQL",
    "postgresql with jsonb columns": "PostgreSQL",
    "postgresql data warehouse": "PostgreSQL",
    "amazon rds for postgresql": "AWS RDS PostgreSQL",
    "amazon rds (postgresql)": "AWS RDS PostgreSQL",
    "aws rds for postgresql": "AWS RDS PostgreSQL",
    "aws rds (postgresql)": "AWS RDS PostgreSQL",
    "aws rds postgresql": "AWS RDS PostgreSQL",
    "rds for postgresql": "AWS RDS PostgreSQL",
    "amazon rds with postgresql": "AWS RDS PostgreSQL",
    "heroku postgres": "Heroku PostgreSQL",
    "render managed postgresql": "Render PostgreSQL",
    "supabase (postgresql)": "Supabase PostgreSQL",
    
    # PostgreSQL with PostGIS
    "postgis": "PostGIS",
    "postgresql with postgis": "PostgreSQL + PostGIS",
    "postgresql (with postgis)": "PostgreSQL + PostGIS",
    "postgresql with postgis extension": "PostgreSQL + PostGIS",
    "postgresql (with postgis extension)": "PostgreSQL + PostGIS",
    "postgresql with postgis extension for spatial data": "PostgreSQL + PostGIS",
    "postgis extension": "PostGIS",
    "postgis extension for postgresql": "PostGIS",
    "postgis on aws rds postgresql": "AWS RDS PostgreSQL + PostGIS",
    "postgresql + postgis": "PostgreSQL + PostGIS",
    
    # PostgreSQL with TimescaleDB
    "timescaledb": "TimescaleDB",
    "postgresql with timescaledb extension": "PostgreSQL + TimescaleDB",
    "postgresql (with timescaledb)": "PostgreSQL + TimescaleDB",
    "timescaledb extension": "TimescaleDB",
    "timescaledb extension for postgresql": "TimescaleDB",
    "timescaledb (postgresql)": "PostgreSQL + TimescaleDB",
    "timescaledb (postgresql extension)": "PostgreSQL + TimescaleDB",
    "timescaledb (as a postgresql extension, managed by aws rds)": "AWS RDS PostgreSQL + TimescaleDB",
    "aws rds for postgresql with timescaledb extension": "AWS RDS PostgreSQL + TimescaleDB",
    "postgresql with the timescaledb extension": "PostgreSQL + TimescaleDB",
    
    # PostgreSQL with pgvector
    "pgvector": "pgvector",
    "postgresql (with pgvector)": "PostgreSQL + pgvector",
    "pgvector (postgresql extension)": "pgvector",
    
    # Amazon Aurora PostgreSQL
    "amazon aurora postgresql": "Amazon Aurora PostgreSQL",
    "amazon aurora (postgresql compatible)": "Amazon Aurora PostgreSQL",
    "amazon aurora (postgresql compatible edition)": "Amazon Aurora PostgreSQL",
    "amazon aurora postgresql-compatible": "Amazon Aurora PostgreSQL",
    "amazon aurora postgresql-compatible edition": "Amazon Aurora PostgreSQL",
    "amazon aurora (postgresql-compatible edition)": "Amazon Aurora PostgreSQL",
    "amazon aurora postgresql compatible edition": "Amazon Aurora PostgreSQL",
    "amazon aurora postgresql (serverless v2)": "Amazon Aurora PostgreSQL",
    "amazon rds aurora postgresql": "Amazon Aurora PostgreSQL",
    "aws aurora postgresql": "Amazon Aurora PostgreSQL",
    "aws aurora (postgresql compatible)": "Amazon Aurora PostgreSQL",
    "aurora postgresql": "Amazon Aurora PostgreSQL",
    "amazon aurora": "Amazon Aurora",
    
    # Redis variants
    "redis": "Redis",
    "redis (aws elasticache for redis)": "AWS ElastiCache Redis",
    "redis (via aws elasticache)": "AWS ElastiCache Redis",
    "redis (via aws elasticache for redis)": "AWS ElastiCache Redis",
    "redis (managed by aws elasticache)": "AWS ElastiCache Redis",
    "amazon elasticache for redis": "AWS ElastiCache Redis",
    "amazon elasticache redis": "AWS ElastiCache Redis",
    "amazon elasticache (redis)": "AWS ElastiCache Redis",
    "aws elasticache for redis": "AWS ElastiCache Redis",
    "aws elasticache (redis)": "AWS ElastiCache Redis",
    "aws elasticache": "AWS ElastiCache",
    "elasticache for redis": "AWS ElastiCache Redis",
    "redis enterprise": "Redis Enterprise",
    "redis cluster": "Redis Cluster",
    "redis queue": "Redis",
    
    # Elasticsearch variants
    "elasticsearch": "Elasticsearch",
    "elasticsearch (aws opensearch)": "AWS OpenSearch",
    "elasticsearch (aws opensearch service)": "AWS OpenSearch",
    "elasticsearch (via aws opensearch service)": "AWS OpenSearch",
    "elasticsearch (managed by aws opensearch service)": "AWS OpenSearch",
    "elasticsearch (aws opensearch service / elastic cloud)": "AWS OpenSearch",
    "elasticsearch / opensearch": "Elasticsearch",
    "elasticsearch (or aws opensearch service)": "Elasticsearch",
    "elasticsearch (or opensearch)": "Elasticsearch",
    "opensearch": "OpenSearch",
    "opensearch (aws opensearch service)": "AWS OpenSearch",
    "opensearch (formerly elasticsearch)": "OpenSearch",
    "amazon opensearch service": "AWS OpenSearch",
    "amazon opensearch service (managed elasticsearch)": "AWS OpenSearch",
    "amazon opensearch service (formerly elasticsearch)": "AWS OpenSearch",
    "amazon opensearch service (formerly elasticsearch service)": "AWS OpenSearch",
    "amazon opensearch service (with vector engine for amazon opensearch service)": "AWS OpenSearch",
    "aws opensearch service": "AWS OpenSearch",
    "aws opensearch service (managed elasticsearch)": "AWS OpenSearch",
    "aws opensearch service (elasticsearch)": "AWS OpenSearch",
    
    # Pinecone variants
    "pinecone": "Pinecone",
    "pinecone (managed service)": "Pinecone",
    
    # ClickHouse variants
    "clickhouse": "ClickHouse",
    
    # Snowflake variants
    "snowflake": "Snowflake",
    "snowflake / google bigquery": "Snowflake",
    
    # Amazon S3 variants
    "amazon s3": "Amazon S3",
    "aws s3": "Amazon S3",
    "s3": "Amazon S3",
    "aws s3 (simple storage service)": "Amazon S3",
    "amazon s3 (simple storage service)": "Amazon S3",
    "aws s3 (amazon simple storage service)": "Amazon S3",
    "amazon s3-compatible object storage": "Amazon S3",
    "aws s3 + efs (elastic file system)": "Amazon S3",
    "aws s3 & cloudfront": "Amazon S3",
    "aws s3 with parquet/delta lake format": "Amazon S3",
    "apache parquet files on aws s3": "Amazon S3",
    "zarr on object storage (e.g., aws s3)": "Amazon S3",
    "parquet files on object storage": "Object Storage",
    
    # BigQuery variants
    "bigquery": "Google BigQuery",
    "google bigquery": "Google BigQuery",
    
    # Redshift variants
    "amazon redshift": "Amazon Redshift",
    "redshift": "Amazon Redshift",
    "aws redshift": "Amazon Redshift",
    "aws redshift spectrum": "Amazon Redshift",
    
    # InfluxDB variants
    "influxdb": "InfluxDB",
    "influxdb cloud": "InfluxDB",
    "influxdb (v2.x)": "InfluxDB",
    
    # DynamoDB variants
    "amazon dynamodb": "Amazon DynamoDB",
    "dynamodb": "Amazon DynamoDB",
    "aws dynamodb": "Amazon DynamoDB",
    "aws dynamodb (nosql)": "Amazon DynamoDB",
    "amazon dynamodb (with dax for caching)": "Amazon DynamoDB",
    
    # Neptune variants
    "amazon neptune": "Amazon Neptune",
    "aws neptune": "Amazon Neptune",
    
    # Firebase variants
    "firebase realtime database": "Firebase Realtime Database",
    "firebase firestore": "Firebase Firestore",
    "firestore": "Firebase Firestore",
    "cloud firestore": "Firebase Firestore",
    "firebase (firestore)": "Firebase Firestore",
    "firebase": "Firebase",
    "firebase storage": "Firebase Storage",
    
    # IPFS variants
    "ipfs": "IPFS",
    "ipfs (interplanetary file system)": "IPFS",
    "ipfs (interplanetary file system) via pinata": "IPFS",
    "ipfs with pinata": "IPFS",
    "ipfs (via pinata or web3.storage)": "IPFS",
    "ipfs / filecoin": "IPFS",
    "ipfs + filecoin": "IPFS",
    "filecoin": "Filecoin",
    "pinata": "Pinata",
    
    # Neo4j variants
    "neo4j": "Neo4j",
    
    # Supabase variants
    "supabase": "Supabase",
    "supabase storage": "Supabase Storage",
    
    # The Graph variants
    "the graph": "The Graph",
    "the graph protocol": "The Graph",
    
    # Apache Druid variants
    "apache druid": "Apache Druid",
    
    # AWS Timestream variants
    "aws timestream": "AWS Timestream",
    "amazon timestream": "AWS Timestream",
    
    # Databricks variants
    "databricks": "Databricks",
    
    # Google Cloud Storage variants
    "google cloud storage": "Google Cloud Storage",
    "google cloud storage (gcs)": "Google Cloud Storage",
    "gcs": "Google Cloud Storage",
    "gcp cloud storage": "Google Cloud Storage",
    
    # SQLite variants
    "sqlite": "SQLite",
    "sqlite3": "SQLite",
    "sqlite (local/dev)": "SQLite",
    
    # MySQL variants
    "mysql": "MySQL",
    
    # Athena variants
    "amazon athena": "Amazon Athena",
    "aws athena": "Amazon Athena",
    "amazon kinesis data firehose + s3 + athena": "Amazon Athena",
    
    # Qdrant variants
    "qdrant": "Qdrant",
    
    # Weaviate variants
    "weaviate": "Weaviate",
    
    # FAISS variants
    "faiss": "FAISS",
    
    # Prometheus variants
    "prometheus": "Prometheus",
    
    # Apache Kafka variants
    "apache kafka": "Apache Kafka",
    "apache kafka (aws msk)": "Apache Kafka",
    "apache kafka (aws msk - managed streaming for apache kafka)": "Apache Kafka",
    
    # AWS Kinesis variants
    "aws kinesis data streams": "AWS Kinesis",
    
    # Amazon SageMaker variants
    "amazon sagemaker feature store": "Amazon SageMaker",
    "aws sagemaker feature store": "Amazon SageMaker",
    
    # DigitalOcean variants
    "digitalocean spaces": "DigitalOcean Spaces",
    
    # Blockchain variants
    "ethereum blockchain": "Ethereum",
    "ethereum": "Ethereum",
    "ethereum mainnet": "Ethereum",
    "ethereum sepolia testnet": "Ethereum",
    "polygon pos chain": "Polygon",
    "polygon (matic)": "Polygon",
    "polygon": "Polygon",
    "polygon blockchain": "Polygon",
    "arbitrum": "Arbitrum",
    "on-chain data": "Blockchain",
    "smart contracts": "Blockchain",
    
    # OrbitDB variants
    "orbitdb": "OrbitDB",
    
    # IndexedDB variants
    "indexeddb": "IndexedDB",
    
    # MinIO variants
    "minio": "MinIO",
    
    # Azure variants
    "azure blob storage": "Azure Blob Storage",
    
    # ChromaDB variants
    "chromadb": "ChromaDB",
    
    # Local Storage variants
    "browser's localstorage": "LocalStorage",
    "browser's localstorage api": "LocalStorage",
    "local storage": "LocalStorage",
    "localstorage": "LocalStorage",
    "browser localstorage": "LocalStorage",
    "browser's local storage": "LocalStorage",
    "browser's `localstorage`": "LocalStorage",
    "browser's `localstorage` api": "LocalStorage",
    "browser local storage": "LocalStorage",
    "web storage (specifically `localstorage`)": "LocalStorage",
    "browser's localstorage for score persistence": "LocalStorage",
    "none (beyond `localstorage`)": "LocalStorage",
    
    # JSON File variants
    "json file": "JSON Files",
    "json files": "JSON Files",
    "static json files": "JSON Files",
    "local json files": "JSON Files",
    "json file on disk": "JSON Files",
    "static json file": "JSON Files",
    "simple json file storage": "JSON Files",
    "json files stored in the codebase": "JSON Files",
    "static json": "JSON Files",
    "json file (static content)": "JSON Files",
    "json file (static data source)": "JSON Files",
    "static json files within the react app": "JSON Files",
    "content will be stored as json files": "JSON Files",
    "simple json file": "JSON Files",
    "json file or in-memory object": "JSON Files",
    "python dictionary / json file": "JSON Files",
    "none (json data structure)": "JSON Files",
    "none (static json/javascript object)": "JSON Files",
    "in-memory javascript array": "JSON Files",
    
    # Elasticsearch variants (additional)
    "elasticsearch": "Elasticsearch",
    "kibana": "Kibana",
    "logstash": "Logstash",
    "loki": "Loki",
    "thanos": "Thanos",
    
    # etcd variants
    "etcd": "etcd",
    
    # Oracle variants
    "oracle": "Oracle",
    
    # Filebase variants
    "filebase": "Filebase",
    
    # ScyllaDB variants
    "scylladb": "ScyllaDB",
    
    # File System variants
    "file system": "File System",
    
    # Hyperledger variants
    "hyperledger fabric": "Hyperledger Fabric",
    "hyperledger fabric's built-in state database": "Hyperledger Fabric",
    "hyperledger fabric's couchdb": "Hyperledger Fabric",
    
    # Ceramic Network variants
    "ceramic network": "Ceramic Network",
    
    # CouchDB variants
    "couchdb": "CouchDB",
    
    # Markdown variants
    "markdown files with front matter": "Markdown Files",
    "git repository (markdown/yaml/json files)": "Git Repository",
    
    # Google Sheets variants
    "google sheets": "Google Sheets",
    "google sheets api": "Google Sheets",
    
    # Algolia variants
    "algolia": "Algolia",
    
    # Arweave variants
    "arweave": "Arweave",
    
    # LevelDB variants
    "leveldb": "LevelDB",
    
    # Apache Hadoop variants
    "apache hadoop": "Apache Hadoop",
    
    # Apache Cassandra variants
    "apache cassandra": "Apache Cassandra",
    "cassandra": "Apache Cassandra",
    
    # Delta Lake variants
    "delta lake": "Delta Lake",
    "apache parquet/delta lake": "Delta Lake",
    
    # Textile variants
    "textile": "Textile",
    
    # AWS QLDB variants
    "aws qldb": "AWS QLDB",
    
    # TensorFlow Serving variants
    "tensorflow serving": "TensorFlow Serving",
    
    # Sanity.io variants
    "sanity.io": "Sanity.io",
    "sanity.io (headless cms)": "Sanity.io",
    "sanity.io's built-in database": "Sanity.io",
    "headless cms": "Headless CMS",
    
    # MLflow variants
    "mlflow": "MLflow",
    
    # Milvus variants
    "milvus": "Milvus",
    
    # Apache Airflow variants
    "apache airflow": "Apache Airflow",
    
    # Cloudinary variants
    "cloudinary": "Cloudinary",
    
    # Annoy variants
    "annoy": "Annoy",
    
    # Git variants
    "git": "Git",
    "git repository": "Git Repository",
    
    # AWS RDS variants
    "aws rds": "AWS RDS",
    "amazon rds": "AWS RDS",
    "rds for sql databases": "AWS RDS",
    
    # None/No Database variants
    "none": "None",
    "none required": "None",
    "none (not required)": "None",
    "none needed": "None",
    "none (explicitly)": "None",
    "no database required": "None",
    "no backend database": "None",
    "no database needed": "None",
    "no database is needed": "None",
    "no traditional database needed": "None",
    "no external database required": "None",
    "not applicable, as static sites do not require databases.": "None",
    "not necessary for this project": "None",
    "not needed": "None",
    "not necessary": "None",
    "not required": "None",
    "no database needed": "None",
    "none required - static data stored in json format": "None",
    "none (static/mocked data)": "None",
    "none required (file-based content)": "None",
    "n/a": "None",
}

# Update TECH_SYNONYMS to use the new databases_synonyms dictionary
TECH_SYNONYMS = {
    'hosting': hosting_synonyms,
    
    'frontend_frameworks': frontend_frameworks_synonyms,
    
    'frontend_styling_solutions': frontend_styling_synonyms,
    
    'frontend_libraries': frontend_libraries_synonyms,
    
    'backend_frameworks': backend_frameworks_synonyms,
    
    'backend_languages': backend_languages_synonyms,
    
    'authentication': authentication_synonyms,
    
    'orms': orms_synonyms,
    
    'databases': databases_synonyms,
    
    'other_tools': {
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "k8s": "Kubernetes",
        "git": "Git",
        "github": "GitHub",
        "gitlab": "GitLab",
        # Add more tools synonyms as needed...
    }
}

# Create comprehensive other tools synonyms dictionary
other_tools_synonyms = {
    # Docker variants
    "docker": "Docker",
    "docker compose": "Docker Compose",
    "docker-compose": "Docker Compose",
    "dockerize": "Docker",
    "containerization": "Docker",
    "docker containers": "Docker",
    "docker swarm": "Docker Swarm",
    
    # Kubernetes variants
    "kubernetes": "Kubernetes",
    "k8s": "Kubernetes",
    "kubectl": "Kubernetes",
    "kubernetes cluster": "Kubernetes",
    "k8s cluster": "Kubernetes",
    "kubernetes orchestration": "Kubernetes",
    "container orchestration": "Kubernetes",
    "helm": "Helm",
    "helm charts": "Helm",
    
    # Git & Version Control
    "git": "Git",
    "github": "GitHub",
    "gitlab": "GitLab",
    "bitbucket": "Bitbucket",
    "github actions": "GitHub Actions",
    "gitlab ci": "GitLab CI",
    "gitlab ci/cd": "GitLab CI/CD",
    "version control": "Git",
    "git version control": "Git",
    "github workflows": "GitHub Actions",
    "github pages": "GitHub Pages",
    "git hooks": "Git Hooks",
    
    # Build Tools & Bundlers
    "webpack": "Webpack",
    "vite": "Vite",
    "rollup": "Rollup",
    "parcel": "Parcel",
    "esbuild": "esbuild",
    "turbopack": "Turbopack",
    "snowpack": "Snowpack",
    "browserify": "Browserify",
    "gulp": "Gulp",
    "grunt": "Grunt",
    "babel": "Babel",
    "swc": "SWC",
    "rome": "Rome",
    "biome": "Biome",
    
    # Testing Tools
    "jest": "Jest",
    "vitest": "Vitest",
    "cypress": "Cypress",
    "playwright": "Playwright",
    "selenium": "Selenium",
    "webdriver": "WebDriver",
    "puppeteer": "Puppeteer",
    "mocha": "Mocha",
    "chai": "Chai",
    "jasmine": "Jasmine",
    "karma": "Karma",
    "enzyme": "Enzyme",
    "react testing library": "React Testing Library",
    "testing library": "Testing Library",
    "storybook": "Storybook",
    "chromatic": "Chromatic",
    "percy": "Percy",
    "backstop": "BackstopJS",
    "testcafe": "TestCafe",
    "nightwatch": "Nightwatch",
    
    # Code Quality & Linting
    "eslint": "ESLint",
    "prettier": "Prettier",
    "tslint": "TSLint",
    "stylelint": "Stylelint",
    "husky": "Husky",
    "lint-staged": "lint-staged",
    "commitlint": "commitlint",
    "commitizen": "Commitizen",
    "semantic-release": "semantic-release",
    "standard": "StandardJS",
    "jshint": "JSHint",
    "jslint": "JSLint",
    "sonarqube": "SonarQube",
    "sonarcloud": "SonarCloud",
    "codeclimate": "CodeClimate",
    "codecov": "Codecov",
    "coveralls": "Coveralls",
    
    # Infrastructure as Code
    "terraform": "Terraform",
    "ansible": "Ansible",
    "chef": "Chef",
    "puppet": "Puppet",
    "saltstack": "SaltStack",
    "vagrant": "Vagrant",
    "packer": "Packer",
    "cloudformation": "CloudFormation",
    "aws cloudformation": "AWS CloudFormation",
    "azure resource manager": "Azure Resource Manager",
    "arm templates": "ARM Templates",
    "bicep": "Bicep",
    "pulumi": "Pulumi",
    "cdk": "AWS CDK",
    "aws cdk": "AWS CDK",
    "serverless framework": "Serverless Framework",
    
    # CI/CD Tools
    "jenkins": "Jenkins",
    "circleci": "CircleCI",
    "travis ci": "Travis CI",
    "azure devops": "Azure DevOps",
    "azure pipelines": "Azure Pipelines",
    "bamboo": "Bamboo",
    "teamcity": "TeamCity",
    "buildkite": "Buildkite",
    "drone": "Drone",
    "concourse": "Concourse",
    "spinnaker": "Spinnaker",
    "argo cd": "ArgoCD",
    "flux": "Flux",
    "tekton": "Tekton",
    "github actions": "GitHub Actions",
    "gitlab ci": "GitLab CI",
    
    # Package Managers
    "npm": "npm",
    "yarn": "Yarn",
    "pnpm": "pnpm",
    "bun": "Bun",
    "pip": "pip",
    "poetry": "Poetry",
    "pipenv": "Pipenv",
    "conda": "Conda",
    "composer": "Composer",
    "bundler": "Bundler",
    "cargo": "Cargo",
    "go mod": "Go Modules",
    "maven": "Maven",
    "gradle": "Gradle",
    "sbt": "SBT",
    "lerna": "Lerna",
    "rush": "Rush",
    "nx": "Nx",
    "turborepo": "Turborepo",
    
    # Development Environment
    "vscode": "VS Code",
    "visual studio code": "VS Code",
    "webstorm": "WebStorm",
    "intellij": "IntelliJ IDEA",
    "sublime text": "Sublime Text",
    "atom": "Atom",
    "vim": "Vim",
    "neovim": "Neovim",
    "emacs": "Emacs",
    "brackets": "Brackets",
    "codepen": "CodePen",
    "codesandbox": "CodeSandbox",
    "stackblitz": "StackBlitz",
    "repl.it": "Replit",
    "gitpod": "Gitpod",
    "github codespaces": "GitHub Codespaces",
    "cloud9": "AWS Cloud9",
    
    # Monitoring & Analytics
    "sentry": "Sentry",
    "bugsnag": "Bugsnag",
    "rollbar": "Rollbar",
    "new relic": "New Relic",
    "datadog": "Datadog",
    "splunk": "Splunk",
    "elk stack": "ELK Stack",
    "elasticsearch": "Elasticsearch",
    "logstash": "Logstash",
    "kibana": "Kibana",
    "grafana": "Grafana",
    "prometheus": "Prometheus",
    "jaeger": "Jaeger",
    "zipkin": "Zipkin",
    "opentelemetry": "OpenTelemetry",
    "google analytics": "Google Analytics",
    "mixpanel": "Mixpanel",
    "amplitude": "Amplitude",
    "hotjar": "Hotjar",
    "fullstory": "FullStory",
    "logrocket": "LogRocket",
    
    # API Development & Testing
    "postman": "Postman",
    "insomnia": "Insomnia",
    "swagger": "Swagger",
    "openapi": "OpenAPI",
    "apidoc": "APIDoc",
    "newman": "Newman",
    "curl": "cURL",
    "httpie": "HTTPie",
    "rest client": "REST Client",
    "graphql playground": "GraphQL Playground",
    "apollo studio": "Apollo Studio",
    
    # Database Tools
    "pgadmin": "pgAdmin",
    "phpmyadmin": "phpMyAdmin",
    "adminer": "Adminer",
    "dbeaver": "DBeaver",
    "navicat": "Navicat",
    "tableplus": "TablePlus",
    "sequel pro": "Sequel Pro",
    "mongodb compass": "MongoDB Compass",
    "robo 3t": "Robo 3T",
    "redis commander": "Redis Commander",
    "redis insight": "RedisInsight",
    
    # Documentation
    "gitbook": "GitBook",
    "notion": "Notion",
    "confluence": "Confluence",
    "mkdocs": "MkDocs",
    "docusaurus": "Docusaurus",
    "vuepress": "VuePress",
    "docsify": "Docsify",
    "sphinx": "Sphinx",
    "jsdoc": "JSDoc",
    "typedoc": "TypeDoc",
    "swagger ui": "Swagger UI",
    "redoc": "ReDoc",
    
    # Communication & Collaboration
    "slack": "Slack",
    "discord": "Discord",
    "microsoft teams": "Microsoft Teams",
    "zoom": "Zoom",
    "jira": "Jira",
    "trello": "Trello",
    "asana": "Asana",
    "monday.com": "Monday.com",
    "linear": "Linear",
    "github issues": "GitHub Issues",
    "gitlab issues": "GitLab Issues",
    
    # Design & Prototyping
    "figma": "Figma",
    "sketch": "Sketch",
    "adobe xd": "Adobe XD",
    "invision": "InVision",
    "zeplin": "Zeplin",
    "abstract": "Abstract",
    "framer": "Framer",
    "principle": "Principle",
    "marvel": "Marvel",
    
    # Security Tools
    "snyk": "Snyk",
    "dependabot": "Dependabot",
    "whitesource": "WhiteSource",
    "veracode": "Veracode",
    "checkmarx": "Checkmarx",
    "owasp zap": "OWASP ZAP",
    "burp suite": "Burp Suite",
    "nessus": "Nessus",
    "qualys": "Qualys",
    
    # Performance Tools
    "lighthouse": "Lighthouse",
    "webpagetest": "WebPageTest",
    "gtmetrix": "GTmetrix",
    "pingdom": "Pingdom",
    "uptime robot": "Uptime Robot",
    "new relic": "New Relic",
    "dynatrace": "Dynatrace",
    "appdynamics": "AppDynamics",
    
    # Mobile Development
    "xcode": "Xcode",
    "android studio": "Android Studio",
    "react native debugger": "React Native Debugger",
    "flipper": "Flipper",
    "expo dev tools": "Expo Dev Tools",
    "ionic devapp": "Ionic DevApp",
    "testflight": "TestFlight",
    "google play console": "Google Play Console",
    "firebase console": "Firebase Console",
    
    # Content Management
    "strapi": "Strapi",
    "contentful": "Contentful",
    "sanity": "Sanity",
    "ghost": "Ghost",
    "wordpress": "WordPress",
    "drupal": "Drupal",
    "joomla": "Joomla",
    "forestry": "Forestry",
    "netlify cms": "Netlify CMS",
    "decap cms": "Decap CMS",
    
    # Email Services
    "sendgrid": "SendGrid",
    "mailgun": "Mailgun",
    "ses": "Amazon SES",
    "amazon ses": "Amazon SES",
    "postmark": "Postmark",
    "mailchimp": "Mailchimp",
    "constant contact": "Constant Contact",
    
    # File Storage & CDN
    "cloudflare": "Cloudflare",
    "fastly": "Fastly",
    "keycdn": "KeyCDN",
    "maxcdn": "MaxCDN",
    "cloudfront": "CloudFront",
    "aws cloudfront": "AWS CloudFront",
    "azure cdn": "Azure CDN",
    "google cloud cdn": "Google Cloud CDN",
    
    # Search Services
    "algolia": "Algolia",
    "elasticsearch": "Elasticsearch",
    "solr": "Apache Solr",
    "swiftype": "Swiftype",
    
    # Form Services
    "typeform": "Typeform",
    "google forms": "Google Forms",
    "jotform": "JotForm",
    "wufoo": "Wufoo",
    "formstack": "Formstack",
    "netlify forms": "Netlify Forms",
    
    # Analytics & Tracking
    "google tag manager": "Google Tag Manager",
    "segment": "Segment",
    "rudderstack": "RudderStack",
    "snowplow": "Snowplow",
    
    # Serverless & Functions
    "serverless": "Serverless Framework",
    "serverless framework": "Serverless Framework",
    "aws sam": "AWS SAM",
    "azure functions": "Azure Functions",
    "google cloud functions": "Google Cloud Functions",
    "netlify functions": "Netlify Functions",
    "vercel functions": "Vercel Functions",
    
    # Blockchain Development
    "hardhat": "Hardhat",
    "truffle": "Truffle",
    "ganache": "Ganache",
    "remix": "Remix IDE",
    "metamask": "MetaMask",
    "web3.js": "Web3.js",
    "ethers.js": "Ethers.js",
    
    # Game Development
    "unity": "Unity",
    "unreal engine": "Unreal Engine",
    "godot": "Godot",
    "construct": "Construct",
    "gamemaker": "GameMaker",
    
    # Machine Learning & AI
    "jupyter": "Jupyter",
    "google colab": "Google Colab",
    "kaggle": "Kaggle",
    "wandb": "Weights & Biases",
    "mlflow": "MLflow",
    "tensorboard": "TensorBoard",
    "apache airflow": "Apache Airflow",
    
    # None/No Tools variants
    "none": "None",
    "none required": "None",
    "not applicable": "None",
    "n/a": "None",
    "no additional tools": "None",
    "standard tools": "Standard Tools",
    "basic tools": "Basic Tools",
    
    # Add more tool synonyms as needed...
}

# Update TECH_SYNONYMS to use the new other_tools_synonyms dictionary
TECH_SYNONYMS = {
    'hosting': hosting_synonyms,
    
    'frontend_frameworks': frontend_frameworks_synonyms,
    
    'frontend_styling_solutions': frontend_styling_synonyms,
    
    'frontend_libraries': frontend_libraries_synonyms,
    
    'backend_frameworks': backend_frameworks_synonyms,
    
    'backend_languages': backend_languages_synonyms,
    
    'authentication': authentication_synonyms,
    
    'orms': orms_synonyms,
    
    'databases': databases_synonyms,
    
    'other_tools': other_tools_synonyms
}

def normalize_technology(tech_name: str, category: str = None) -> str:
    """
    Normalize a technology name by mapping it to its canonical form.
    
    Args:
        tech_name (str): The technology name to normalize
        category (str, optional): The technology category to search in. If None, searches all categories.
        
    Returns:
        str: The normalized/canonical technology name
    """
    if not tech_name:
        return tech_name
    
    # Convert to lowercase for case-insensitive matching
    tech_lower = tech_name.lower().strip()
    
    # If category is specified, only search in that category
    if category and category in TECH_SYNONYMS:
        return TECH_SYNONYMS[category].get(tech_lower, tech_name)
    
    # Otherwise, search all categories
    for cat_synonyms in TECH_SYNONYMS.values():
        if tech_lower in cat_synonyms:
            return cat_synonyms[tech_lower]
    
    # Return original if no match found
    return tech_name 