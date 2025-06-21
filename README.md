# AI Content Assistant Pro

**AI Content Assistant Pro** este o aplicație web simplă, construită cu Streamlit, concepută pentru a ajuta creatorii de conținut să optimizeze titlurile video pentru platforme precum TikTok, YouTube și Meta. Aplicația generează sugestii de hashtag-uri și descrieri pe baza titlului video introdus și a limbii selectate.

## Funcționalități curente (v1.2)

*   **Generare SEO pe bază de titlu**: Introduceți titlul videoclipului dvs. și aplicația va genera:
    *   **Hashtag-uri relevante**: Include hashtag-uri generice (#ai, #contentcreator), un hashtag specific limbii (de ex., #romanavideo), și hashtag-uri derivate din cuvintele cheie ale titlului.
    *   **Descrieri adaptate**: Generează o scurtă descriere care încorporează titlul video și menționează optimizarea pentru limba aleasă.
*   **Suport multilingv**:
    *   Interfața utilizatorului și conținutul generat sunt disponibile în:
        *   Română (Implicit)
        *   Engleză
        *   Maghiară
    *   Selecția limbii adaptează atât textele din interfață, cât și sugestiile SEO.
*   **Interfață simplă și intuitivă**: Construită cu Streamlit pentru ușurință în utilizare.

## Tehnologii utilizate

*   **Python**: Limbajul de programare principal.
*   **Streamlit**: Framework-ul folosit pentru a construi interfața web interactivă.

## Cum se rulează local

1.  **Cerințe preliminare**:
    *   Python 3.7+ instalat.
    *   `pip` (Python package installer).

2.  **Clonați repository-ul (dacă este cazul)**:
    ```bash
    git clone <URL_REPOSITORY>
    cd <NUME_DIRECTOR_REPOSITORY>
    ```

3.  **Creați și activați un mediu virtual (recomandat)**:
    ```bash
    python -m venv venv
    # Pe Windows:
    # venv\Scripts\activate
    # Pe macOS/Linux:
    # source venv/bin/activate
    ```

4.  **Instalați dependențele**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Rulați aplicația Streamlit**:
    ```bash
    streamlit run app.py
    ```
    Aplicația ar trebui să se deschidă automat în browserul dvs. web.

## Contribuții

Momentan, proiectul este într-un stadiu incipient. Sugestiile și contribuțiile sunt binevenite pe măsură ce proiectul evoluează.

## Roadmap (Idei pentru viitor)

*   Integrare cu modele lingvistice avansate (LLMs) pentru generare SEO de calitate superioară.
*   Analiza tendințelor pentru sugestii de hashtag-uri.
*   Opțiuni de personalizare avansate (public țintă, tonul vocii etc.).
*   Salvarea și gestionarea istoricului de căutări.

---
*Powered by ChatGPT (conceptual) - v1.2*
