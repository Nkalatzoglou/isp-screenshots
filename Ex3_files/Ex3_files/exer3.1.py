
import wave
def extract_lsb(audio_file):
    #Open file AND frames read
    with wave.open(audio_file, 'rb') as audio:
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    #Extract the LSB from each byte
    extracted_bits = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

    #Bit array to byte array to string convert
    hidden_data = "".join(chr(int("".join(map(str, extracted_bits[i:i+8])), 2)) for i in range(0, len(extracted_bits), 8))

    hidden_data = hidden_data.split("###")[0]

    return hidden_data

hidden_message = extract_lsb("Ex3_sound1.wav")
print("Hidden message:", hidden_message)
