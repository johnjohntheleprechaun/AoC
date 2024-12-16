let
    pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/cf8cc1201be8bc71b7cbbbdaf349b22f4f99c7ae.tar.gz") {};
in pkgs.mkShell {
    packages = with pkgs; [
        (python312.withPackages (python-pkgs: with pkgs.python312Packages; [
            numpy
        ]))
    ];
}
