use encoding_rs::GBK;

#[derive(serde::Serialize)]
struct FileResult {
    path: String,
    content: String,
}

#[tauri::command]
fn read_item_file() -> Result<FileResult, String> {
    let path = rfd::FileDialog::new()
        .add_filter("数据文件", &["txt"])
        .set_title("选择 ItemInfo.txt")
        .pick_file();

    let Some(path) = path else {
        return Ok(FileResult { path: String::new(), content: String::new() });
    };

    let bytes = std::fs::read(&path).map_err(|e| e.to_string())?;
    let (text, _, had_errors) = GBK.decode(&bytes);
    let content = if !had_errors {
        text.into_owned()
    } else {
        String::from_utf8(bytes)
            .map_err(|_| "无法解码文件：不是 GBK 或 UTF-8 编码".to_string())?
    };

    Ok(FileResult {
        path: path.to_string_lossy().to_string(),
        content,
    })
}

#[tauri::command]
fn save_item_file(path: String, content: String) -> Result<(), String> {
    let (encoded, _, _) = GBK.encode(&content);
    std::fs::write(&path, encoded.as_ref()).map_err(|e| e.to_string())
}

#[tauri::command]
fn read_character_file() -> Result<FileResult, String> {
    let path = rfd::FileDialog::new()
        .add_filter("数据文件", &["txt"])
        .set_title("选择 CharacterInfo.txt")
        .pick_file();

    let Some(path) = path else {
        return Ok(FileResult { path: String::new(), content: String::new() });
    };

    let bytes = std::fs::read(&path).map_err(|e| e.to_string())?;
    let (text, _, had_errors) = GBK.decode(&bytes);
    let content = if !had_errors {
        text.into_owned()
    } else {
        String::from_utf8(bytes)
            .map_err(|_| "无法解码文件：不是 GBK 或 UTF-8 编码".to_string())?
    };

    Ok(FileResult {
        path: path.to_string_lossy().to_string(),
        content,
    })
}

#[tauri::command]
fn save_character_file(path: String, content: String) -> Result<(), String> {
    let (encoded, _, _) = GBK.encode(&content);
    std::fs::write(&path, encoded.as_ref()).map_err(|e| e.to_string())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![read_item_file, save_item_file, read_character_file, save_character_file])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
