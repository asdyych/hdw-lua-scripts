use encoding_rs::GBK;

#[tauri::command]
fn read_item_file() -> Result<String, String> {
    let path = rfd::FileDialog::new()
        .add_filter("Text files", &["txt"])
        .set_title("Select ItemInfo.txt")
        .pick_file();

    let Some(path) = path else {
        return Ok(String::new());
    };

    let bytes = std::fs::read(&path).map_err(|e| e.to_string())?;

    // Try GBK first (common for this game's data files)
    let (text, _, had_errors) = GBK.decode(&bytes);
    if !had_errors {
        return Ok(text.into_owned());
    }

    // Fall back to UTF-8
    String::from_utf8(bytes).map_err(|_| "Cannot decode file: not GBK or UTF-8".to_string())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![read_item_file])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
