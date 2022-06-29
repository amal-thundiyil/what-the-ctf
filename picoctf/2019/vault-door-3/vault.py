def checkPassword(password):
    if (len(password) != 32) {
        return false;
    }
     buffer = new char[32];
    int i;
    for (i=0; i<8; i++) {
        buffer[i] = password[i]
    }
    for (; i<16; i++) {
        buffer[i] = password[23-i]
    }
    for (; i<32; i+=2) {
        buffer[i] = password[46-i]
    }
    for (i=31; i>=17; i-=2) {
        buffer[i] = password[i]
    }
    s = new String(buffer]
    return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f")
