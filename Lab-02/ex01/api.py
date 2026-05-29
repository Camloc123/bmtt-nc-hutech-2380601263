# pyrefly: ignore [missing-import]
from flask import Flask, request, jsonify
from flask_cors import CORS

from cipher.caesar import CaesarCipher 
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher



app = Flask(__name__)

CORS(app)

caesar_cipher = CaesarCipher() 
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher  = PlayfairCipher()

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "success", "message": "Cipher API is running perfectly!"})


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.get_json()
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu tham số plain_text hoặc key'}), 400
            
        plain_text = data['plain_text']
        key = int(data['key'])
        
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_message' : encrypted_text})
    except ValueError:
        return jsonify({'error': 'Key của thuật toán Caesar phải là một số nguyên'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/caesar/decrypt", methods=["POST"]) 
def caesar_decrypt():
    try:
        data = request.get_json()
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu tham số cipher_text hoặc key'}), 400
            
        cipher_text = data['cipher_text']
        key = int(data['key'])
        
        decrypt_text = caesar_cipher.decrypt_text(cipher_text, key) 
        return jsonify({'decrypted_message' : decrypt_text})
    except ValueError:
        return jsonify({'error': 'Key của thuật toán Caesar phải là một số nguyên'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    try:
        data = request.get_json()
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu tham số plain_text hoặc key'}), 400
            
        plain_text = data['plain_text']
        key = data['key']
        
        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        return jsonify({'encrypted_message' : encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    try:
        data = request.get_json()
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu tham số cipher_text hoặc key'}), 400
            
        cipher_text = data['cipher_text']
        key = data['key']
        
        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
        return jsonify({'decrypted_message' : decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    try:
        data = request.get_json()
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu tham số plain_text hoặc key'}), 400
            
        plain_text = data['plain_text']
        key = int(data['key'])
        
        encrypted_text = railfence_cipher.railfence_encrypt(plain_text, key)
        return jsonify({'encrypted_message' : encrypted_text})
    except ValueError:
        return jsonify({'error': 'Key của thuật toán Railfence phải là một số nguyên'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    try:
        data = request.get_json()
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu tham số cipher_text hoặc key'}), 400
            
        cipher_text = data['cipher_text']
        key = int(data['key'])
        
        decrypted_text = railfence_cipher.railfence_decrypt(cipher_text, key)
        return jsonify({'decrypted_message' : decrypted_text})
    except ValueError:
        return jsonify({'error': 'Key của thuật toán Railfence phải là một số nguyên'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    try:
        data = request.get_json()
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu tham số plain_text hoặc key'}), 400
            
        plain_text = data['plain_text']
        key = data['key']
        
        pf_cipher = PlayfairCipher(key)
        encrypted_text = pf_cipher.encrypt(plain_text)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    try:
        data = request.get_json()
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Thiếu tham số cipher_text hoặc key'}), 400
            
        cipher_text = data['cipher_text']
        key = data['key']
        
        pf_cipher = PlayfairCipher(key)
        
        # Gọi hàm decrypt từ class PlayfairCipher
        decrypted_text = pf_cipher.decrypt(cipher_text) 
        return jsonify({'decrypted_message': decrypted_text})
    
    except AttributeError:
         return jsonify({'error': 'Hàm decrypt() chưa được định nghĩa trong file class PlayfairCipher của bạn'}), 501
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True)