Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Rcon = [0x00000000,
        0x01000000, 0x02000000, 0x04000000, 0x08000000,
        0x10000000, 0x20000000, 0x40000000, 0x80000000,
        0x1B000000, 0x36000000, 0x6C000000, 0xD8000000,
        0xAB000000, 0x4D000000, 0x9A000000, 0x2F000000,
        0x5E000000, 0xBC000000, 0x63000000, 0xC6000000,
        0x97000000, 0x35000000, 0x6A000000, 0xD4000000,
        0xB3000000, 0x7D000000, 0xFA000000, 0xEF000000,
        0xC5000000, 0x91000000, 0x39000000, 0x72000000,
        0xE4000000, 0xD3000000, 0xBD000000, 0x61000000,
        0xC2000000, 0x9F000000, 0x25000000, 0x4A000000,
        0x94000000, 0x33000000, 0x66000000, 0xCC000000,
        0x83000000, 0x1D000000, 0x3A000000, 0x74000000,
        0xE8000000, 0xCB000000, 0x8D000000]

def ffAdd(a, b): return a ^ b

def xtime(a):
    leftmostbit = a & 0x80      # For checking left-most bit
    a <<= 1                     # multiply by x

    if leftmostbit == 0x80:     # Left-most bit was set
        a ^= 0x11b              # Polynomial x^8+x^4+x^3+x+1
    return a

def ffMultiply(a, b):
    p, xtime_result = 0, a

    for i in range(8):
        if (b & 1 == 1):
            p ^= xtime_result
        xtime_result = xtime(xtime_result)
        b >>= 1
    
    return p

def subWord(fourByteInput):
    output = 0x00
    mask = 0xFF000000
    shift = 24

    for i in range(4):
        byte = Sbox[(fourByteInput & mask) >> shift]
        output = (output << 8) ^ byte
        mask >>= 8
        shift -= 8

    return output

def rotWord(fourByteInput):
    output = 0x00
    leftMostByte = (fourByteInput & 0xFF000000) >> 24
    mask = 0xFF0000
    shift = 16

    for i in range(3):
        byte = (fourByteInput & mask) >> shift
        output = (output << 8) ^ byte
        mask >>= 8
        shift -= 8

    output = (output << 8) ^ leftMostByte
    return output       
    
def subBytes(state):
    for r in range(4):
        for c in range(4):
            state[r][c] = Sbox[state[r][c]]
    return state

def invSubBytes(state):
    for r in range(4):
        for c in range(4):
            state[r][c] = InvSbox[state[r][c]]
    return state

def shiftRows(state):
    # shift row 1
    temp = state[1][0]
    state[1][0] = state[1][1]; state[1][1] = state[1][2]; state[1][2] = state[1][3]; state[1][3] = temp 

    # shift row 2
    for i in range(2):
        temp = state[2][0]
        state[2][0] = state[2][1]; state[2][1] = state[2][2]; state[2][2] = state[2][3]; state[2][3] = temp 

    # shift row 3
    for i in range(3):
        temp = state[3][0]
        state[3][0] = state[3][1]; state[3][1] = state[3][2]; state[3][2] = state[3][3]; state[3][3] = temp
    
    return state

def invShiftRows(state):
    # shift row 1
    temp = state[1][3]
    state[1][3] = state[1][2]; state[1][2] = state[1][1]; state[1][1] = state[1][0]; state[1][0] = temp

    # shift row 2
    for i in range(2):
        temp = state[2][3]
        state[2][3] = state[2][2]; state[2][2] = state[2][1]; state[2][1] = state[2][0]; state[2][0] = temp
    
    # shift row 3
    for i in range(3):
        temp = state[3][3]
        state[3][3] = state[3][2]; state[3][2] = state[3][1]; state[3][1] = state[3][0]; state[3][0] = temp
    
    return state

def mixColumns(state):
    state_prime = [[], [], [], []]

    for c in range(4): 
        state_prime[0].append(ffMultiply(0x02, state[0][c]) ^ ffMultiply(0x03, state[1][c]) ^ state[2][c] ^ state[3][c])
        state_prime[1].append(state[0][c] ^ ffMultiply(0x02, state[1][c]) ^ ffMultiply(0x03, state[2][c]) ^ state[3][c]) 
        state_prime[2].append(state[0][c] ^ state[1][c] ^ ffMultiply(0x02, state[2][c]) ^ ffMultiply(0x03, state[3][c]))
        state_prime[3].append(ffMultiply(0x03, state[0][c]) ^ state[1][c] ^ state[2][c] ^ ffMultiply(0x02, state[3][c])) 

    return state_prime

def invMixColumns(s):
    state_prime = [[], [], [], []]

    for c in range(4):
        state_prime[0].append(ffMultiply(0x0e, s[0][c]) ^ ffMultiply(0x0b, s[1][c]) ^ ffMultiply(0x0d, s[2][c]) ^ ffMultiply(0x09, s[3][c]))
        state_prime[1].append(ffMultiply(0x09, s[0][c]) ^ ffMultiply(0x0e, s[1][c]) ^ ffMultiply(0x0b, s[2][c]) ^ ffMultiply(0x0d, s[3][c]))
        state_prime[2].append(ffMultiply(0x0d, s[0][c]) ^ ffMultiply(0x09, s[1][c]) ^ ffMultiply(0x0e, s[2][c]) ^ ffMultiply(0x0b, s[3][c]))    
        state_prime[3].append(ffMultiply(0x0b, s[0][c]) ^ ffMultiply(0x0d, s[1][c]) ^ ffMultiply(0x09, s[2][c]) ^ ffMultiply(0x0e, s[3][c]))

    return state_prime

def KeyExpansion(key, Nk, Nb, Nr):
    w = []

    for i in range(Nk):
        word = 0x00; word = (word << 8) ^ key[4*i]; word = (word << 8) ^ key[4*i+1]; word = (word << 8) ^ key[4*i+2]; word = (word << 8) ^ key[4*i+3]
        w.append(word)

    i = Nk
    while (i < (Nb * (Nr + 1))):        
        temp = w[i-1]
        
        if (i % Nk == 0): temp = subWord(rotWord(temp)) ^ Rcon[(int)(i/Nk)]
        elif (Nk > 6 and (i % Nk == 4)): temp = subWord(temp)

        w.append(w[i-Nk] ^ temp)
        i += 1

    return w

def formatState(state):
    formattedState = 0x00

    for c in range(4):
        for r in range(4):
            formattedState ^= state[r][c]
            if(r != 3 or c != 3): formattedState <<= 8

    return formattedState

def createWMatrix(w, l, rN):
    new_w = [[],[],[],[]]
    for c in range(4):
        new_w[0].append((w[l+c] >> 24) & 0xFF)
        new_w[1].append((w[l+c] >> 16) & 0xFF)
        new_w[2].append((w[l+c] >> 8) & 0xFF)
        new_w[3].append(w[l+c] & 0xFF)

    print('{:032x}'.format(int(formatState(new_w))))
    return new_w

def addRoundKey(state, w, rN, Nb):
    l = rN * Nb
    new_w = createWMatrix(w, l, rN)
    for c in range(4):
        for r in range(4):
            state[r][c] ^= new_w[r][c]

    return state

def Cipher (plain, w, Nb, Nr):
    state = [[],[],[],[]]
    rN = 0

    print("round[ 0].input    ", '{:032x}'.format(int(plain)))
    # Read plain into 4x4 array of state
    for c in range(4):
        for r in range(4):
            state[r].append((plain & 0xFF000000000000000000000000000000) >> 120)
            plain <<= 8

    # Call addRoundKey with state, w, rN = 0, Nb
    print(f"round[ 0].k_sch     ", end="")
    state = addRoundKey(state, w, rN, Nb);      print("round[ 1].start    ", '{:032x}'.format(int(formatState(state))))

    # Complete rounds
    for rN in range(1, Nr):
        subBytes(state);                        print(f"round[{rN:2d}].s_box    ", '{:032x}'.format(int(formatState(state))))
        shiftRows(state);                       print(f"round[{rN:2d}].s_row    ", '{:032x}'.format(int(formatState(state))))
        state = mixColumns(state);              print(f"round[{rN:2d}].m_col    ", '{:032x}'.format(int(formatState(state))))
        
        print(f"round[{rN:2d}].k_sch     ", end="") 
        state = addRoundKey(state, w, rN, Nb);  print(f"round[{rN+1:2d}].start    ", '{:032x}'.format(int(formatState(state))))

    # Complete last round
    subBytes(state);                            print(f"round[{Nr:2d}].s_box    ", '{:032x}'.format(int(formatState(state))))
    shiftRows(state);                           print(f"round[{Nr:2d}].s_row    ", '{:032x}'.format(int(formatState(state))))
    
    print(f"round[{Nr:2d}].k_sch     ", end="")
    state = addRoundKey(state, w, Nr, Nb);      print(f"round[{Nr:2d}].output   ", '{:032x}'.format(int(formatState(state))))

    # Reformat cipher with state

    return formatState(state)

def InvCipher(cipher, w, Nb, Nr):
    state = [[],[],[],[]]
    rN = Nr

    print("round[ 0].iinput   ", '{:032x}'.format(int(cipher)))
    for c in range(4):
        for r in range(4):
            state[r].append((cipher & 0xFF000000000000000000000000000000) >> 120)
            cipher <<= 8

    # Call addRoundKey with state, w, rN = 0, Nb
    print(f"round[ 0].ik_sch    ", end="")
    state = addRoundKey(state, w, rN, Nb);      print("round[ 1].istart   ", '{:032x}'.format(int(formatState(state))))

    # Complete rounds
    for i in range(1, Nr):
        rN -= 1
        invShiftRows(state);                       print(f"round[{i:2d}].is_row   ", '{:032x}'.format(int(formatState(state))))       
        invSubBytes(state);                        print(f"round[{i:2d}].is_box   ", '{:032x}'.format(int(formatState(state))))
        
        print(f"round[{i:2d}].ik_sch    ", end="")
        state = addRoundKey(state, w, rN, Nb);     print(f"round[{i:2d}].ik_add   ", '{:032x}'.format(int(formatState(state))))
        state = invMixColumns(state);              print(f"round[{i+1:2d}].istart   ", '{:032x}'.format(int(formatState(state))))

    # Complete last round
    invShiftRows(state);                           print(f"round[{Nr:2d}].is_row   ", '{:032x}'.format(int(formatState(state))))
    invSubBytes(state);                            print(f"round[{Nr:2d}].is_box   ", '{:032x}'.format(int(formatState(state))))
    
    print(f"round[{Nr:2d}].ik_sch    ", end="")
    state = addRoundKey(state, w, rN-1, Nb);       print(f"round[{Nr:2d}].ioutput  ", '{:032x}'.format(int(formatState(state))))

    return formatState(state)

def main():
    
    # ----- EXAMPLE 1: AES-128 (Nk = 4, Nr = 10) -----#
    k = 0x000102030405060708090a0b0c0d0e0f
    plain = 0x00112233445566778899aabbccddeeff
    key = []

    Nk = 4 # Length of key can be 4, 6, 8
    Nb = 4 # Number of bytes, always 4
    Nr = 10 # Number of rounds. Cn be 10, 12, 14

    # Divide key into array of size 4 * Nk
    for i in range(Nk * Nb):
        mask = 0xFF000000000000000000000000000000
        key.append((k & mask) >> 120)
        k <<= 8

    w = KeyExpansion(key, Nk, Nb, Nr)

    print("C.1   AES-128 (Nk=4, Nr=10)\n")

    print("PLAINTEXT:          00112233445566778899aabbccddeeff")
    print("KEY:                000102030405060708090a0b0c0d0e0f\n")

    print("CIPHER (ENCRYPT):")
    cipher = Cipher(plain, w, Nb, Nr)
    print("\nINVERSE CIPHER (DECRYPT):")
    plain = InvCipher(cipher, w, Nb, Nr)


    # ----- EXAMPLE 2: AES-192 (Nk = 6, Nr = 12) -----#
    k = 0x000102030405060708090a0b0c0d0e0f1011121314151617
    key = []

    Nk = 6 # Length of key can be 4, 6, 8
    Nr = 12 # Number of rounds. Cn be 10, 12, 14

    # Divide key into array of size 4 * Nk
    for i in range(Nk * Nb):
        mask = 0xFF0000000000000000000000000000000000000000000000
        key.append((k & mask) >> 184)
        k <<= 8

    w = KeyExpansion(key, Nk, Nb, Nr)

    print("\nC.2   AES-192 (Nk=6, Nr=12)\n")

    print("PLAINTEXT:          00112233445566778899aabbccddeeff")
    print("KEY:                000102030405060708090a0b0c0d0e0f1011121314151617\n")

    print("CIPHER (ENCRYPT):")
    cipher = Cipher(plain, w, Nb, Nr)
    print("\nINVERSE CIPHER (DECRYPT):")
    plain = InvCipher(cipher, w, Nb, Nr)


    # ----- EXAMPLE 3: AES-256 (Nk = 8, Nr = 14) -----#
    k = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
    key = []

    Nk = 8 # Length of key can be 4, 6, 8
    Nr = 14 # Number of rounds. Cn be 10, 12, 14

    # Divide key into array of size 4 * Nk
    for i in range(Nk * Nb):
        mask = 0xFF00000000000000000000000000000000000000000000000000000000000000
        key.append((k & mask) >> 248)
        k <<= 8

    w = KeyExpansion(key, Nk, Nb, Nr)

    print("\nC.3   AES-256 (Nk=8, Nr=14)\n")

    print("PLAINTEXT:          00112233445566778899aabbccddeeff")
    print("KEY:                000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f\n")

    print("CIPHER (ENCRYPT):")
    cipher = Cipher(plain, w, Nb, Nr)
    print("\nINVERSE CIPHER (DECRYPT):")
    plain = InvCipher(cipher, w, Nb, Nr)


if __name__ == "__main__":
    main()