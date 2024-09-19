import argparse
import glob
import plistlib
import sys
import uuid


def font_payload(reverse_dns, font_path, i):
    with open(font_path, "rb") as f:
        return {
            "PayloadType": "com.apple.font",
            "PayloadVersion": 1,
            "PayloadIdentifier": f"{reverse_dns}.font{i}",
            "PayloadUUID": str(uuid.uuid4()),
            "Font": f.read(),
        }


def main(name, pattern, output, reverse_dns, no_consent_text):
    data = {
        "PayloadContent": [
            font_payload(reverse_dns, f, i)
            for i, f in enumerate(glob.glob(pattern), start=1)
        ],
        "PayloadDescription": f"Provides the {name} fonts.",
        "PayloadDisplayName": f"{name} fonts",
        "PayloadIdentifier": reverse_dns,
        "PayloadUUID": str(uuid.uuid4()),
        "PayloadType": "Configuration",
        "PayloadVersion": 1,
        "ConsentText": {
            "default": f"Only install this profile if you trust the source and you are fully compliant with the license agreement of the {name} fonts.",
        },
    }

    if no_consent_text:
        del data["ConsentText"]

    if output:
        with open(output, "xb") as f:
            plistlib.dump(data, f)
    else:
        print(plistlib.dumps(data).decode("utf-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--name", help="font name", required=True)
    parser.add_argument("-p", "--pattern", help="font file glob pattern", required=True)
    parser.add_argument("-o", "--output", help="output file")
    parser.add_argument(
        "-r",
        "--reverse-dns-prefix",
        help="reverse dns prefix",
        default=f"com.example.installfont.{str(uuid.uuid4()).replace('-', '')}",
    )
    parser.add_argument(
        "--no-consent-text",
        help="disable consent text",
        action="store_true",
        default=False,
    )

    args = parser.parse_args()

    try:
        main(
            args.name,
            args.pattern,
            args.output,
            args.reverse_dns_prefix,
            args.no_consent_text,
        )
    except FileExistsError:
        sys.exit(f"Error: {args.output} already exists.")
    except Exception as e:
        sys.exit(f"Error: {e}")
