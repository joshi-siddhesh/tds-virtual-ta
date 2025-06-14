{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.requests
    pkgs.python311Packages.beautifulsoup4
    pkgs.python311Packages.playwright
    pkgs.python311Packages.fastapi
    pkgs.python311Packages.uvicorn
  ];
}
