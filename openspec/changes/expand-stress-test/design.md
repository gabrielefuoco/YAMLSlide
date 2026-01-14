# Design: Expand Stress Test

## Overview
Questo documento dettaglia le specifiche YAML per ogni nuova slide da aggiungere al comprehensive stress test.

---

## Nuove Slide Proposte

### 10. Grid 2-col con Mix di Contenuti
```yaml
- type: "grid"
  layout: "2-col"
  title: "Grid 2 Colonne: Mix Contenuti"
  lead: "COSA VEDERE: Due colonne bilanciate con contenuti misti (testo e liste)."
  cards:
    - title: "Card Testuale"
      text: |
        Questa card contiene **solo testo** con formattazione Markdown.
        
        Supporta paragrafi multipli e `codice inline`.
    - title: "Card con Lista"
      items:
        - "Elemento con **grassetto**"
        - "Elemento con *corsivo*"
        - "Elemento con `code`"
        - "Elemento con [link](https://example.com)"
```

### 11. Chart Line - Andamento Temporale
```yaml
- type: "chart"
  title: "Grafico a Linee: Trend"
  lead: "COSA VEDERE: Una linea continua che mostra valori nel tempo."
  chart_type: "line"
  labels: ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu"]
  data: [65, 59, 80, 81, 56, 95]
  dataset_label: "Progresso Mensile"
```

### 12. Chart Pie - Torta
```yaml
- type: "chart"
  title: "Grafico a Torta: Distribuzione"
  lead: "COSA VEDERE: Fette colorate proporzionali ai valori."
  chart_type: "pie"
  labels: ["Frontend", "Backend", "DevOps", "Design"]
  data: [40, 30, 20, 10]
  dataset_label: "Team Allocation"
```

### 13. Chart Doughnut - Ciambella
```yaml
- type: "chart"
  title: "Grafico Doughnut: Vuoto al Centro"
  lead: "COSA VEDERE: Come la torta ma con buco centrale."
  chart_type: "doughnut"
  labels: ["React", "Vue", "Angular", "Svelte"]
  data: [50, 25, 15, 10]
  dataset_label: "Framework Usage"
```

### 14. Split text-right - Layout Invertito
```yaml
- type: "split"
  title: "Split: Testo a Destra"
  layout: "text-right"
  image_url: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop"
  content: |
    ### COSA VEDERE:
    * L'immagine deve essere a **sinistra**
    * Il testo deve essere a **destra**
    * Questo testa il layout invertito rispetto alla slide 5
    
    > "Il codice è poesia in movimento."
```

### 15. Table Inline - Dati Diretti
```yaml
- type: "table"
  title: "Tabella Inline: Dati YAML"
  lead: "COSA VEDERE: Tabella generata da dati definiti direttamente nel YAML."
  columns: ["Feature", "Status", "Priority", "Owner"]
  rows:
    - ["Dark Theme", "✅ Done", "P0", "Team A"]
    - ["Animations", "✅ Done", "P1", "Team B"]
    - ["Export PDF", "🔄 WIP", "P2", "Team A"]
    - ["Live Reload", "❌ TODO", "P3", "Team C"]
    - ["Mobile View", "🔄 WIP", "P1", "Team B"]
```

### 16. Mermaid Sequence - Diagramma di Sequenza
```yaml
- type: "mermaid"
  title: "Sequence Diagram: Flusso Autenticazione"
  code: |
    sequenceDiagram
      participant U as User
      participant A as App
      participant S as Server
      U->>A: Click Login
      A->>S: POST /auth
      S-->>A: JWT Token
      A-->>U: Welcome!
```

### 17. Code JavaScript - Linguaggio Diverso
```yaml
- type: "code"
  title: "JavaScript: Async/Await"
  language: "javascript"
  code: |
    // COSA VEDERE: Sintassi JS con colori appropriati
    async function fetchData(url) {
      try {
        const response = await fetch(url);
        const data = await response.json();
        return data;
      } catch (error) {
        console.error('Failed:', error);
        throw error;
      }
    }
```

### 18. Code Rust - Altro Linguaggio
```yaml
- type: "code"
  title: "Rust: Memory Safety"
  language: "rust"
  code: |
    // COSA VEDERE: Sintassi Rust con colori distinti
    fn main() {
        let greeting = String::from("Hello, YAMLSlide! 🦀");
        println!("{}", greeting);
        
        let numbers: Vec<i32> = (1..=10).collect();
        let sum: i32 = numbers.iter().sum();
        println!("Sum: {}", sum);
    }
```

### 19. Hero con Titolo Lungo
```yaml
- type: "hero"
  title: "Stress Test: <span style='color: #f472b6;'>Titolo Estremamente Lungo</span> per Verificare l'Overflow"
  subtitle: "Questo sottotitolo è intenzionalmente verboso per testare come il layout gestisce contenuti testuali molto estesi che potrebbero superare la larghezza normale della viewport."
  meta_info:
    label: "Stress Level"
    value: "MAXIMUM OVERDRIVE"
    badge: "EDGE-CASE-TEST"
```

### 20. Process con 5 Step
```yaml
- type: "process"
  title: "Pipeline a 5 Fasi: Stress Layout"
  steps:
    - header: "Step 1"
      title: "Ideazione"
      text: "Brainstorming e definizione obiettivi."
    - header: "Step 2"
      title: "Design"
      text: "Creazione mockup e specifiche."
    - header: "Step 3"
      title: "Sviluppo"
      text: "Implementazione del codice."
    - header: "Step 4"
      title: "Testing"
      text: "QA e validazione."
    - header: "Step 5"
      title: "Deploy"
      text: "Messa in produzione."
  footer_badges:
    title: "Stack Utilizzato"
    items: ["Python", "Jinja2", "HTML5", "CSS3", "JavaScript"]
```

### 21. Grid con Markdown Estremo
```yaml
- type: "grid"
  layout: "2-col"
  title: "Markdown Stress Test"
  lead: "COSA VEDERE: Tutte le formattazioni Markdown supportate."
  cards:
    - title: "Formattazione Testo"
      text: |
        **Bold** e *italic* e ~~strikethrough~~
        
        `inline code` e [link](https://example.com)
        
        > Citazione con stile
    - title: "Simboli & Unicode"
      items:
        - "Emoji: 🚀 🎨 ⚡ 🔥 💎 🌈"
        - "Entità: &amp; &lt; &gt; &copy; &reg;"
        - "Unicode: ñ ü ö ä ß æ ø å"
        - "RTL Test: مرحبا שלום"
        - "Math: ∑∏∫∂∇∆Ω"
```

### 22. Mermaid Pie Chart
```yaml
- type: "mermaid"
  title: "Mermaid Pie: Distribuzione Risorse"
  code: |
    pie showData
      title Resource Allocation
      "CPU" : 45
      "Memory" : 30
      "Storage" : 15
      "Network" : 10
```

---

## Palette Colori Alternativa (Test)

Per testare diversi schemi cromatici, propongo di modificare anche la sezione `theme` con una palette ancora più estrema e aggiungere radial_layers addizionali:

```yaml
theme:
  bg_primary: "#0a0a0a"           # Nero quasi puro
  accent_primary: "#00ff88"        # Verde Neon (Matrix)
  accent_secondary: "#ff00ff"      # Magenta
  accent_tertiary: "#00ffff"       # Cyan
  text_primary: "#ffffff"          # Bianco puro
  text_secondary: "#888888"        # Grigio medio
```

---

## Considerazioni Tecniche

1. **Grid 4-col**: Al momento il template supporta solo `2-col` e `3-col`. Se si vuole testare 4 colonne, servirà prima aggiungere il CSS class `.grid-4`.

2. **Chart Types**: Chart.js supporta bar, line, pie, doughnut, radar, polarArea. Quelli testati saranno line, pie, doughnut.

3. **Mermaid Diagrams**: Il tema è già impostato su `dark`. I diagrammi sequence, pie e class dovrebbero renderizzare correttamente.

4. **Unicode & Emoji**: I caratteri speciali richiedono il corretto font-family (Inter supporta la maggior parte).
