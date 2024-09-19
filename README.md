# installfont

**installfont** allows you to install fonts on an Apple device without having to use a third-party app that costs money
or might contain ads, trackers or other unwanted things. It's a script that generates a configuration profile and should
run out-of-the-box on a reasonably modern Python (though I only tested it with Python 3.12 running on macOS).

> **Side quest alert!** It also works on [iSH][] (which has Python 3.9) if you're feeling brave. That said,
> **installfont** won't specifically support it.

I would like to thank Apple for providing the [Configuration Profile Reference][cpr], which is very thorough and without
which this script would been impossible to write.

## Usage

```
usage: installfont.py [-h] -n NAME -p PATTERN [-o OUTPUT] [-r REVERSE_DNS_PREFIX] [--no-consent-text]

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  font name
  -p PATTERN, --pattern PATTERN
                        font file glob pattern
  -o OUTPUT, --output OUTPUT
                        output file
  -r REVERSE_DNS_PREFIX, --reverse-dns-prefix REVERSE_DNS_PREFIX
                        reverse dns prefix
  --no-consent-text     disable consent text
```

For example:

```bash
python3 installfont.py \
    --name "Fira Code" \
    --pattern "/Users/julia/Downloads/Fira_Code_v6.2/ttf/FiraCode-*.ttf" \
    --output "FiraCode.mobileconfig" \
    --reverse-dns-prefix "io.github.heyajulia"
```

> [!WARNING]
>
> The profile is not signed. This is OK as long as you've created it yourself or you trust the person who sent it to
> you.

> [!IMPORTANT]
>
> Make sure to quote the pattern so it will be expanded by the script and not by your shell.

Then you can transfer it to your device in a convenient way (e.g. `python3 -m http.server`, etc.) and open it. Your
device should guide you through the installation process.

> [!TIP]
>
> You may need to quit and reopen the app in which you want to use the font.

> [!NOTE]
>
> By default, the script will add a "consent" screen that pops up during profile installation and explains what the
> profile does and reminds you that you should only install profiles you trust and only include fonts you have the right
> to use. You can disable this screen using the `--no-consent-text` option.

## License

**installfont** is released under the terms of the 0-clause BSD license. See the LICENSE file for more information.

[ish]: https://ish.app/
[cpr]: https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf
