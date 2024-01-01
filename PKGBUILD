# Maintainer: Pavlos Orfanidis <pavlos@orfanidis.net.gr>

pkgname=turingmachine.pro
pkgver=1.0.0
pkgrel=1
pkgdesc="Run any Turing machine possible using this app"
arch=('any')
url="https://turingmachine.pro"
license=('custom')
depends=('python')
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::git+https://github.com/porfanid/turingMachinePremium.git")
sha256sums=('SKIP')  # You need to calculate the actual checksum

prepare() {
  cd "$srcdir" || return 1

  # Clone the Git repository
  git clone https://github.com/porfanid/turingMachinePremium.git "$pkgname-$pkgver" || return 1
}

package() {
  cd "$srcdir/$pkgname-$pkgver" || return 1

  # Install the Python scripts
  install -Dm755 turingmachine.pro.py "$pkgdir/usr/bin/turingmachine.pro/turingmachine.pro.py"
  install -Dm755 ui_form.py "$pkgdir/usr/bin/turingmachine.pro/ui_form.py"
  install -Dm755 ui_license_import.py "$pkgdir/usr/bin/turingmachine.pro/ui_license_import.py"
  install -Dm755 requirements.txt "$pkgdir/usr/bin/turingmachine.pro/requirements.txt"

  install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # Create a virtual environment
  python -m venv "$pkgdir/usr/bin/turingmachine.pro/venv"

  # Install dependencies in the virtual environment
  "$pkgdir/usr/bin/turingmachine.pro/venv/bin/pip" install -r "$pkgdir/usr/bin/turingmachine.pro/requirements.txt"

  # Set permissions
  chmod +x "$pkgdir/usr/bin/turingmachine.pro/turingmachine.pro.py"
  chmod +x "$pkgdir/usr/bin/turingmachine.pro/ui_form.py"
  chmod +x "$pkgdir/usr/bin/turingmachine.pro/ui_license_import.py"

  # Install the desktop file
  # Generate the desktop file
  mkdir -p "$pkgdir/usr/share/applications/"
  touch "$pkgdir/usr/share/applications/turingmachine.pro.desktop"
  cat > "$pkgdir/usr/share/applications/turingmachine.pro.desktop" <<EOL
[Desktop Entry]
Name=Turing Machine Pro
Exec=/usr/bin/turingmachine.pro/venv/bin/python3 /usr/bin/turingmachine.pro/turingmachine.pro.py
Icon=/usr/share/icons/turingmachine.pro.jpg
Type=Application
Categories=Utility;
EOL

  # Install the icon
  install -Dm644 turingmachine.pro.jpg "$pkgdir/usr/share/icons/turingmachine.pro.jpg"
}
