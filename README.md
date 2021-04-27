# <h1 align="center">EZ Skin Price Aggregator 🧧</h1>

A tool that collects skin prices from various marketplaces.

<p align="center">
  <img src="https://i.ibb.co/YtQTZRB/data.png">
</p>

## Introduction
Python and a few libraries are necessary to run the file. I will explain how to download the libraries later in the text.

### Prerequisites
- [Python 3.8](https://www.python.org/downloads/) or newer
- C++ compiler, [this video tutorial](https://youtu.be/ZixCyiMVFqc) can help
- Patience to actually read everything slowly

### Installing
[Click here](https://github.com/cjxe/EZ-skin-price-aggregator/archive/main.zip) to download **or** copy:
```
git clone https://github.com/cjxe/EZ-skin-price-aggregator
``` 
and right click on the terminal (cmd) to paste. 

⚠️ **Do not forget** to install the necessary libraries.

To do that:
- If you are on **Windows**, run `runmeWINDOWS.bat`.
- If you are on **Linux**, paste `pip install -r requirements.txt` into the terminal.

## Usage
![search_query_breakdown](https://i.ibb.co/qjRMyhf/data.png)

After **downloading Python 3.8<** and **the necessary libraries**, run `main.py` and enter a search query in the following manner:

#### 1- Define the `Category`
| What to write | Category it searches in |
|--------|---------------------------------|
| `st` | StatTrak™ and ★ StatTrak™ |
| `so` | Souvenir | (`/pm {username} {text}`) |
| ` ` (nothing, just search without it) | Normal and ★ | 

#### 2- Define the `Weapon`
It can be either one-worded or two-worded, the ultimate amazing brilliant (which is actually better than valve's) search engine knows how to detect the name of the weapon.

**Some examples:**
| What you write | Machine will correct it to |
|--------|---------------------------------|
| `ak 47` | `AK-47` |
| `ak-47` | `AK-47` |
| `ak47` | `AK-47` |
| `aK-47` | `AK-47` |
| `p 2000` | `P2000` |
| `p-2000` | `P2000` |
| `P2000` | `P2000` |
...


#### 3- Define the `Skin`
Once again, it can be either one-worded or two-worded. The ultimate amazing brilliant (which is actually better than valve's) search engine knows how to detect the name of the skin.

**Some examples:**
| What you write | Machine will correct it to |
|--------|---------------------------------|
| `hyperbeast` | `Hyper Beast` |
| `hyper beast` |`Hyper Beast` |
| `HyPeR BeAsT` | `Hyper Beast` |
| `ultra violet` | `Ultraviolet` |
| `ultraviolet` | `Ultraviolet` |
| `ultravi` | `Ultraviolet` |
...


#### 4- Define the `Exterior` (aka `Condition`, `Wear`)
| What to write | Exterior |
|--------|---------------------------------|
| `va` | vanilla (aka `not painted`) |
| `fn` | Factory New |
| `mw` | Minimal Wear |
| `ft` | Field-Tested |
| `ww` | Well-Worn |
| `bs` | Battle-Scarred |

#### 5- Wait and pray for no errors
YALLAH 🙏🙏🙏🙏🙏

#### 6- Check out `./data/search_result.csv` for more info
Yes.

## To-do List
#### Marketplaces to add
- [X] Steam Community Market
- [X] BitSkins
- [ ] ByNoGame
- [ ] BUFF
- [ ] CS.MONEY
- [ ] Skinport

#### Other
- [ ] Pull knives from a database. (`data_scraper.py`)
- [ ] Update weapons and skins when ran once. (`updater.py`)
- [ ] Optimise the search function with the new json file. (`lookups.py`)
- [ ] UI with Electron?..


## Found a bug or want to contribute?
- For bugs and requests please create a new issue [here](https://github.com/cjxe/EZ-skin-price-aggregator/issues).

## License
This app is licensed with GNU General Public License v3.0. **Please** let me know if you are going to use it commercially, thx.

![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fgithub.com%2Fcjxe%2FEZ-skin-price-aggregator)
