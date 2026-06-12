# pyrefly: ignore [missing-import]
from flask import Flask, request, jsonify
from flask_cors import CORS

from cipher.caesar import CaesarCipher 
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.Playfair.playfair_cipher import PlayfairCipher


app = Flask(__name__)

CORS(app)

caesar_cipher = CaesarCipher() 
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "success", "message": "Cipher API is running perfectly!"})

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Không nhận được dữ liệu JSON"
            }), 400

        plain_text = data.get("plain_text")
        key = data.get("key")

        if plain_text is None or key is None:
            return jsonify({
                "error": "Thiếu tham số plain_text hoặc key"
            }), 400

        if not str(plain_text).strip():
            return jsonify({
                "error": "Plain Text không được để trống"
            }), 400

        try:
            key = int(key)
        except (ValueError, TypeError):
            return jsonify({
                "error": "Key phải là số nguyên"
            }), 400

        if key < 1 or key > 25:
            return jsonify({
                "error": "Key phải nằm trong khoảng từ 1 đến 25"
            }), 400

        encrypted_text = caesar_cipher.encrypt_text(
            plain_text,
            key
        )

        return jsonify({
            "encrypted_message": encrypted_text,
            "encrypted_text": encrypted_text
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Không nhận được dữ liệu JSON"
            }), 400

        cipher_text = data.get("cipher_text")
        key = data.get("key")

        if cipher_text is None or key is None:
            return jsonify({
                "error": "Thiếu tham số cipher_text hoặc key"
            }), 400

        if not str(cipher_text).strip():
            return jsonify({
                "error": "Cipher Text không được để trống"
            }), 400

        try:
            key = int(key)
        except (ValueError, TypeError):
            return jsonify({
                "error": "Key phải là số nguyên"
            }), 400

        if key < 1 or key > 25:
            return jsonify({
                "error": "Key phải nằm trong khoảng từ 1 đến 25"
            }), 400

        decrypted_text = caesar_cipher.decrypt_text(
            cipher_text,
            key
        )

        return jsonify({
            "decrypted_message": decrypted_text,
            "decrypted_text": decrypted_text
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Không nhận được dữ liệu JSON"
            }), 400

        plain_text = data.get("plain_text")
        key = data.get("key")

        if plain_text is None or key is None:
            return jsonify({
                "error": "Thiếu tham số plain_text hoặc key"
            }), 400

        encrypted_text = vigenere_cipher.vigenere_encrypt(
            plain_text,
            key
        )

        return jsonify({
            "plain_text": plain_text,
            "key": key,
            "encrypted_message": encrypted_text,
            "encrypted_text": encrypted_text
        }), 200

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Không nhận được dữ liệu JSON"
            }), 400

        cipher_text = data.get("cipher_text")
        key = data.get("key")

        if cipher_text is None or key is None:
            return jsonify({
                "error": "Thiếu tham số cipher_text hoặc key"
            }), 400

        decrypted_text = vigenere_cipher.vigenere_decrypt(
            cipher_text,
            key
        )

        return jsonify({
            "cipher_text": cipher_text,
            "key": key,
            "decrypted_message": decrypted_text,
            "decrypted_text": decrypted_text
        }), 200

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                'error': 'Không nhận được dữ liệu JSON'
            }), 400

        if 'plain_text' not in data:
            return jsonify({
                'error': 'Thiếu tham số plain_text'
            }), 400

        if 'key' not in data:
            return jsonify({
                'error': 'Thiếu tham số key'
            }), 400

        plain_text = data['plain_text']

        try:
            key = int(data['key'])
        except:
            return jsonify({
                'error': 'Key của thuật toán Rail Fence phải là số nguyên'
            }), 400

        encrypted_text = railfence_cipher.railfence_encrypt(
            plain_text,
            key
        )

        return jsonify({
            'encrypted_message': encrypted_text,
            'encrypted_text': encrypted_text
        }), 200

    except ValueError as e:
        return jsonify({
            'error': str(e)
        }), 400

    except Exception as e:
        return jsonify({
            'error': f'Lỗi hệ thống: {str(e)}'
        }), 500


@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                'error': 'Không nhận được dữ liệu JSON'
            }), 400

        if 'cipher_text' not in data:
            return jsonify({
                'error': 'Thiếu tham số cipher_text'
            }), 400

        if 'key' not in data:
            return jsonify({
                'error': 'Thiếu tham số key'
            }), 400

        cipher_text = data['cipher_text']

        try:
            key = int(data['key'])
        except:
            return jsonify({
                'error': 'Key của thuật toán Rail Fence phải là số nguyên'
            }), 400

        decrypted_text = railfence_cipher.railfence_decrypt(
            cipher_text,
            key
        )

        return jsonify({
            'decrypted_message': decrypted_text,
            'decrypted_text': decrypted_text
        }), 200

    except ValueError as e:
        return jsonify({
            'error': str(e)
        }), 400

    except Exception as e:
        return jsonify({
            'error': f'Lỗi hệ thống: {str(e)}'
        }), 500
@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    try:
        if request.is_json:
            data = request.get_json() or {}
        else:
            data = request.form or {}

        plain_text = data.get("inputPlainText") or data.get("plain_text")
        key = data.get("inputKeyPlain") or data.get("key")

        if not key or str(key).strip() == "":
            raise ValueError("Playfair Cipher: Key không được để trống.")

        key = str(key).replace(" ", "").upper()

        if not key.isalpha():
            raise ValueError("Playfair Cipher: Key chỉ được chứa chữ cái A-Z.")

        if not plain_text or str(plain_text).strip() == "":
            raise ValueError("Playfair Cipher: Plain Text không được để trống.")

        plain_text = str(plain_text).replace(" ", "").upper()

        if not plain_text.isalpha():
            raise ValueError("Playfair Cipher: Plain Text chỉ được chứa chữ cái A-Z.")

        pf_cipher = PlayfairCipher(key)
        encrypted_text = pf_cipher.encrypt(plain_text)

        return jsonify({
            "encrypted_message": encrypted_text,
            "encrypted_text": encrypted_text,
            "warnings": pf_cipher.warnings
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500 
@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    try:
        if request.is_json:
            data = request.get_json() or {}
        else:
            data = request.form or {}

        cipher_text = data.get("inputCipherText") or data.get("cipher_text")
        key = data.get("inputKeyCipher") or data.get("key")

        if not key or str(key).strip() == "":
            raise ValueError("Playfair Cipher: Key không được để trống.")

        key = str(key).replace(" ", "").upper()

        if not key.isalpha():
            raise ValueError("Playfair Cipher: Key chỉ được chứa chữ cái A-Z.")

        if not cipher_text or str(cipher_text).strip() == "":
            raise ValueError("Playfair Cipher: Cipher Text không được để trống.")

        cipher_text = str(cipher_text).replace(" ", "").upper()

        if not cipher_text.isalpha():
            raise ValueError("Playfair Cipher: Cipher Text chỉ được chứa chữ cái A-Z.")

        if len(cipher_text) % 2 != 0:
            raise ValueError("Playfair Cipher: Cipher Text phải có độ dài chẵn.")

        pf_cipher = PlayfairCipher(key)
        decrypted_text = pf_cipher.decrypt(cipher_text)

        return jsonify({
            "decrypted_message": decrypted_text,
            "decrypted_text": decrypted_text
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    try:
        if request.is_json:
            data = request.get_json() or {}
        else:
            data = request.form or {}
        key = data.get("key")

        if not key or str(key).strip() == "":
            raise ValueError("Playfair Cipher: Key không được để trống.")

        key = str(key).replace(" ", "").upper()

        if not key.isalpha():
            raise ValueError("Playfair Cipher: Key chỉ được chứa chữ cái A-Z.")

        pf_cipher = PlayfairCipher(key)

        return jsonify({
            "playfair_matrix": pf_cipher.matrix
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True)