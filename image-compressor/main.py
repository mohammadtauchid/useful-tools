import sys

def main():
  if len(sys.argv) != 3:
    print("Usage: python main.py <compression_type> <image_path>")
    return
  
  if sys.argv[1] == "lossy":
    from lossy import compress
  elif sys.argv[1] == "lossless":
    from lossless import compress
  else:
    print("Compression type not supported")
    return
  
  compress(sys.argv[2])

if __name__== "__main__":
  main()