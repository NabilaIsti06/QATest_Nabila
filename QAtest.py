from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inisialisasi WebDriver (untuk Chrome)
driver = webdriver.Chrome()

try:
    # 1. Buka halaman utama Tokopedia
    driver.get("https://www.tokopedia.com")
    time.sleep(2)  # Tunggu halaman beranda untuk dimuat
    
    # Verifikasi bahwa halaman Tokopedia telah dibuka
    assert "Tokopedia" in driver.title

    # 2. Cari produk "Sample Product"
    search_box = driver.find_element(By.NAME, "q")  # Cari kotak pencarian
    search_box.send_keys("Sample Product")  # Masukkan nama produk
    search_box.send_keys(Keys.RETURN)  # Tekan Enter untuk pencarian
    time.sleep(3)  # Tunggu hasil pencarian dimuat

    # 3. Klik pada produk pertama yang ditemukan
    first_product = driver.find_element(By.XPATH, '(//div[@data-testid="master-product-card"])[1]')  # Temukan produk pertama
    first_product.click()
    time.sleep(3)  # Tunggu halaman produk dimuat

    # 4. Tambahkan produk ke keranjang belanja
    add_to_cart_button = driver.find_element(By.XPATH, '//button[contains(text(), "Tambah ke Keranjang")]')
    add_to_cart_button.click()
    time.sleep(2)

    # 5. Verifikasi bahwa produk ada di keranjang
    cart_button = driver.find_element(By.XPATH, '//a[contains(@href, "cart")]')  # Tombol ke halaman keranjang
    cart_button.click()
    time.sleep(3)
    
    # Verifikasi produk "Sample Product" ada di keranjang
    cart_item = driver.find_element(By.XPATH, "//span[contains(text(), 'Sample Product')]")
    assert "Sample Product" in cart_item.text

    # 6. Lanjut ke halaman checkout
    checkout_button = driver.find_element(By.XPATH, '//button[contains(text(), "Checkout")]')  # Tombol Checkout
    checkout_button.click()
    time.sleep(3)

    # Verifikasi produk di halaman checkout
    checkout_item = driver.find_element(By.XPATH, "//span[contains(text(), 'Sample Product')]")
    assert "Sample Product" in checkout_item.text

finally:
    driver.quit()  # Tutup browser setelah selesai
