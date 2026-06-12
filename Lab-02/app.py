from flask import Flask, render_template, request, json
from ex01.cipher.caesar import CaesarCipher
# Import thêm class PlayfairCipher (giả định bạn đã tạo class này trong file playfair.py)
from ex01.cipher.Playfair import PlayfairCipher
from ex01.cipher.vigenere import VigenereCipher
from ex01.cipher.railfence import RailFenceCipher

app = Flask(__name__)

# ==========================================
# ROUTES FOR HOME PAGE
# ==========================================
@app.route("/")
def home():
    return render_template('index.html')


# ==========================================
# ROUTES FOR CAESAR CIPHER
# ==========================================
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ==========================================
# ROUTES FOR PLAYFAIR CIPHER
# ==========================================
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair_encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain'] # KHÔNG ép kiểu int() vì key là chuỗi chữ cái
    
    Playfair = PlayfairCipher(key)
    
    # Sử dụng hàm encrypt của class PlayfairCipher
    encrypted_text = Playfair.encrypt(text)
    
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair_decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher'] # KHÔNG ép kiểu int()
   
    Playfair = PlayfairCipher(key) 
    decrypted_text = Playfair.decrypt(text)
    
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


@app.route("/api/playfair/encrypt", methods=['POST'])
def api_playfair_encrypt():
    try:
        text = request.form.get('inputPlainText', '')
        key = request.form.get('inputKeyPlain', '')
        
        if not key.strip():
            return json.jsonify({"error": "Playfair Cipher: Key không được để trống."}), 400
            
        Playfair = PlayfairCipher(key)
        encrypted_text = Playfair.encrypt(text)
        return json.jsonify({
            "encrypted_message": encrypted_text,
            "encrypted_text": encrypted_text,
            "warnings": Playfair.warnings
        })
    except Exception as e:
        return json.jsonify({"error": str(e)}), 400

@app.route("/api/playfair/decrypt", methods=['POST'])
def api_playfair_decrypt():
    try:
        text = request.form.get('inputCipherText', '')
        key = request.form.get('inputKeyCipher', '')
        
        if not key.strip():
            return json.jsonify({"error": "Playfair Cipher: Key không được để trống."}), 400
            
        Playfair = PlayfairCipher(key)
        decrypted_text = Playfair.decrypt(text)
        return json.jsonify({
            "decrypted_message": decrypted_text,
            "decrypted_text": decrypted_text
        })
    except Exception as e:
        return json.jsonify({"error": str(e)}), 400



# ==========================================
# ROUTES FOR VIGENERE CIPHER
# ==========================================
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere_encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere_decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ==========================================
# ROUTES FOR RAIL FENCE CIPHER
# ==========================================
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    try:
        key = int(request.form['inputKeyPlain'])
    except ValueError:
        return "Key must be an integer"
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.railfence_encrypt(text, key)
    return encrypted_text

@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    try:
        key = int(request.form['inputKeyCipher'])
    except ValueError:
        return "Key must be an integer"
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.railfence_decrypt(text, key)
    return decrypted_text

# ==========================================
# MAIN FUNCTION
# ==========================================
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)