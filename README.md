# Compression & Encryption Project

This project demonstrates the impact of compression and encryption order on different types of files, utilizing several compression and encryption algorithms.

### Libraries

The project uses the `steap-by-steap` library for compression and encryption algorithms. Install it via pip:

```bash
pip install steap-by-steap
```

For more information on `steap-by-steap`, visit the [GitHub repository](https://github.com/jero98772/steap_by_steap).

### Running the Project

To run the project:

```bash
python main.py
```

### Supported File Types

The project supports three types of files:
- **Binary Files**
- **Image Files**
- **Plain Text Files**

### Compression Methods

This project includes the following compression methods:

- **LZW Compression**: A dictionary-based compression algorithm effective for repetitive data, such as plain text.
- **Image FFT (Fast Fourier Transform)**: Used for image compression by transforming image data to the frequency domain.
- **Huffman Compression**: A variable-length encoding algorithm that compresses data based on frequency. This works best with text data where character frequency varies significantly.

For additional details on these methods, refer to the [documentation](https://jero98772.github.io/steap_by_steap/steap_by_steap/compression/index.html).

### Encryption Methods

The project uses the following encryption algorithms:

- **XOR Encryption**: A simple encryption that toggles bits with an XOR operation.
- **Caesar Cipher**: A basic shift cipher.
- **RSA Encryption**: A public-key encryption system that is secure but may increase file size after encryption.

## Conclusions

### Does the Order of Compression and Encryption Matter?

Yes, the effectiveness of compression and encryption can depend on the file type and the specific algorithms used. Some examples include:

- **Huffman Compression**: Effective for plain text due to the frequency-based nature of text data (where some characters appear more often). However, it is less effective for images, where a broad range of colors reduces compression efficiency.
  
- **LZW Compression**: This algorithm groups characters based on repeated patterns, which is more effective for text. When combined with RSA encryption, the encrypted output is larger, as RSA encryption typically expands data.
  
- **Image FFT and Caesar Cipher**: We applied FFT to images followed by Caesar encryption. The Caesar cipher, while simple, added a layer of obfuscation without significantly increasing the image size, making it a suitable option for demonstration purposes.


### Summary

This project demonstrates that the order and choice of compression and encryption algorithms matter and depend on the file type.

The order of compression and encryption does not depend on the file type itself, but rather on its content. For example, when encrypting text, we could use Huffman compression to reduce the size significantly. However, if we’re working with a book like *Don Quixote*, where there aren’t many repeated words, compression won’t be as effective. In this case, we might compress the plain text using Huffman and then encrypt it with RSA. The RSA encryption generally increases the file size because it replaces characters with large numbers (often over 1000) and introduces patterns within these numbers. Therefore, compressing an already encrypted file won’t guarantee a smaller file size.

Alternatively, we could consider XOR encryption combined with LZW compression, which compresses by grouping patterns. In binary files, we often find bit groups that represent meaningful information (like compiled files), as opposed to random sequences of 1s and 0s. In this structured scenario, LZW compression would be effective, and applying XOR encryption afterward would not interfere with the compression. However, if the file type were changed to plain text, the order of compression and encryption would indeed impact the result.

In cases like FFT (Fast Fourier Transform) compression combined with Caesar cipher encryption, the order does not affect the outcome, though this method is impractical and mostly for aesthetic purposes.

In summary, whether compression and encryption order matters depends on the specific content of the file.
