import json
import yaml

def main():
    with open("projects.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    with open("projects.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Wrote projects.json from projects.yaml")

if __name__ == "__main__":
    main()
