import wave
import random

def embed_message_enhanced(audio_file, message, output_file, key):
    random.seed(key)
    with wave.open(audio_file, 'rb') as audio:
        frames = bytearray(list(audio.readframes(audio.getnframes())))
        params = audio.getparams()

    message += '###'
    message_bits = ''.join([bin(ord(c)).lstrip('0b').rjust(8, '0') for c in message])
    indices = random.sample(range(len(frames)), len(message_bits))

    for i, bit in zip(indices, message_bits):
        frames[i] = (frames[i] & 0xFE) | int(bit)

    with wave.open(output_file, 'wb') as modified_audio:
        modified_audio.setparams(params)
        modified_audio.writeframes(frames)

# Example usage
embed_message_enhanced('Ex3_sound5.wav', 'Father Christmas does not exist', 'stego_audio_enhanced.wav', key=1234)

def extract_message_enhanced(stego_audio_file, key):
    random.seed(key)
    with wave.open(stego_audio_file, 'rb') as audio:
        frames = bytearray(list(audio.readframes(audio.getnframes())))

    indices = random.sample(range(len(frames)), len(frames))
    message_bits = [str(frames[i] & 1) for i in indices]

    message = ''.join(chr(int(''.join(message_bits[i:i+8]), 2)) for i in range(0, len(message_bits), 8))
    return message.split('###')[0]

# Example usage
extracted_message = extract_message_enhanced('stego_audio_enhanced.wav', key=1234)
print("Extracted message:", extracted_message)
