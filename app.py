
import streamlit as st

# Configuration
SUPPORTED_LANGUAGES = ["Română", "Engleză", "Maghiară"]
APP_VERSION = "v1.2" # Incremented version

# --- Internationalization (i18n) ---
# Simple dictionary-based i18n
# Keys: lang_code, text_key
# Example: TEXTS['en']['app_title']
TEXTS = {
    "Română": {
        "app_title": "🤖 AI Content Assistant Pro",
        "app_subheader": "Optimizează-ți video-urile pentru TikTok, YouTube și Meta",
        "form_video_title_label": "Titlu video",
        "form_language_label": "Limbă",
        "form_submit_button": "Generează SEO",
        "warning_empty_title": "Te rugăm să introduci un titlu pentru video.",
        "success_seo_generated": "🔍 SEO generat pentru titlul: '{title}' în limba {lang}",
        "suggested_hashtags_header": "**Hashtag-uri sugerate:**",
        "suggested_description_header": "**Descriere sugerată:**",
        "footer_powered_by": "Powered by ChatGPT (conceptual)",
        "desc_template": "Descoperă cum '{title}' te poate ajuta să îți crești vizibilitatea! Acest video este optimizat pentru {lang}.",
        "desc_fallback": "Conținut pentru '{title}' în {lang}.",
    },
    "Engleză": {
        "app_title": "🤖 AI Content Assistant Pro",
        "app_subheader": "Optimize your videos for TikTok, YouTube, and Meta",
        "form_video_title_label": "Video Title",
        "form_language_label": "Language",
        "form_submit_button": "Generate SEO",
        "warning_empty_title": "Please enter a title for the video.",
        "success_seo_generated": "🔍 SEO generated for title: '{title}' in {lang}",
        "suggested_hashtags_header": "**Suggested Hashtags:**",
        "suggested_description_header": "**Suggested Description:**",
        "footer_powered_by": "Powered by ChatGPT (conceptual)",
        "desc_template": "Discover how '{title}' can help you increase your visibility! This video is optimized for {lang}.",
        "desc_fallback": "Content for '{title}' in {lang}.",
    },
    "Maghiară": {
        "app_title": "🤖 AI Tartalom Asszisztens Pro",
        "app_subheader": "Optimalizáld videóidat TikTokra, YouTube-ra és Metára",
        "form_video_title_label": "Videó címe",
        "form_language_label": "Nyelv",
        "form_submit_button": "SEO generálása",
        "warning_empty_title": "Kérjük, adj meg egy címet a videóhoz.",
        "success_seo_generated": "🔍 SEO generálva a '{title}' címhez, {lang} nyelven",
        "suggested_hashtags_header": "**Javasolt hashtagek:**",
        "suggested_description_header": "**Javasolt leírás:**",
        "footer_powered_by": "Powered by ChatGPT (koncepcionális)",
        "desc_template": "Fedezd fel, hogyan segíthet '{title}' a láthatóságod növelésében! Ez a videó {lang} nyelvre van optimalizálva.",
        "desc_fallback": "Tartalom '{title}' címhez, {lang} nyelven.",
    }
}

def get_text(lang: str, key: str, **kwargs) -> str:
    """
    Retrieves a text string for the given language and key from the TEXTS dictionary.
    Allows for basic templating with kwargs.
    """
    try:
        text = TEXTS[lang][key]
        return text.format(**kwargs)
    except KeyError:
        # Fallback to English if the language or key is not found, then to a generic message
        try:
            text = TEXTS["Engleză"][key]
            return text.format(**kwargs)
        except KeyError:
            return f"Missing translation for: {lang} - {key}"

def generate_seo_content(title: str, lang: str) -> tuple[list[str], str]:
    """
    Generates SEO content (hashtags and description) based on the video title and language.
    """
    # Basic hashtag generation
    hashtags = ["#ai", "#contentcreator", f"#{lang.lower().replace('ă', 'a')}video"] # Normalize lang for hashtag
    if title:
        title_words = title.lower().split()
        for word in title_words:
            # Remove common punctuation for cleaner hashtags
            cleaned_word = ''.join(filter(str.isalnum, word))
            if len(cleaned_word) > 3:
                hashtags.append(f"#{cleaned_word}")

    # Description generation using i18n
    if title:
        description = get_text(lang, "desc_template", title=title, lang=lang)
    else: # Should not happen if title is validated, but as a fallback
        description = get_text(lang, "desc_fallback", title="N/A", lang=lang)

    return list(set(hashtags)), description # Return unique hashtags

def main():
    """
    Main function to run the Streamlit application.
    """
    # Determine language for UI (can be set by user, here we use the selected language for content)
    # For a full i18n UI, language selection might be separate or app-wide.
    # Here, we'll use the language selected in the form for UI text where applicable.

    # Initial language for the selectbox itself (before form submission)
    # This part of the UI will remain in the default language of the browser/system or Streamlit's default.
    # To fully translate the UI before any interaction, more complex Streamlit session state management is needed.

    # We default to Romanian for the initial UI elements that are hardcoded before language selection.
    # A more robust solution would involve detecting browser language or having a global language selector.
    _L = "Română" # Default language for the initial UI
    if 'selected_language' in st.session_state:
        _L = st.session_state.selected_language

    st.set_page_config(page_title=get_text(_L, "app_title"), layout="centered")
    st.title(get_text(_L, "app_title"))
    st.subheader(get_text(_L, "app_subheader"))

    with st.form("seo_form"):
        video_title = st.text_input(get_text(_L, "form_video_title_label"))
        # The selectbox label itself will use _L, options are always the language names.
        language_options = SUPPORTED_LANGUAGES
        selected_language_for_content = st.selectbox(
            get_text(_L, "form_language_label"),
            language_options,
            index=language_options.index(_L) if _L in language_options else 0, # Set default selection
            key="selected_language_for_form" # Use a key to access this specific selection
        )
        generate_button = st.form_submit_button(get_text(_L, "form_submit_button"))

    if generate_button:
        # Update session state for UI language to match content language upon generation
        st.session_state.selected_language = selected_language_for_content
        _L = selected_language_for_content # Update _L for subsequent UI text

        if not video_title:
            st.warning(get_text(_L, "warning_empty_title"))
        else:
            st.success(get_text(_L, "success_seo_generated", title=video_title, lang=_L))

            hashtags, description = generate_seo_content(video_title, _L)

            st.write(get_text(_L, "suggested_hashtags_header"))
            st.write(", ".join(hashtags))

            st.write(get_text(_L, "suggested_description_header"))
            st.write(description)

            # Refresh the page with updated language for UI elements outside the form logic
            # This is a bit of a hack for Streamlit; proper i18n often needs more involved state management.
            # For this basic implementation, we rely on the fact that after generation, _L is updated.
            # If we wanted the entire UI to change language *before* generation, that's more complex.
            if st.session_state.selected_language != _L : # if language changed by selection
                 st.experimental_rerun()


    st.markdown("---")
    st.caption(f"{APP_VERSION} • {get_text(_L, 'footer_powered_by')}")

if __name__ == "__main__":
    main()
