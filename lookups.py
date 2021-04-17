import ast
from pyxdameraulevenshtein import damerau_levenshtein_distance_seqs, normalized_damerau_levenshtein_distance_seqs

def we_name(search_query):
    splitted_usr_inp = search_query.split(' ')
    weapon = ''
    skin = ''
    weapons = ['Knife', 'Bayonet', 'Flip Knife', 'Gut Knife', 'Karambit', 'M9 Bayonet', 'Huntsman Knife', 'Butterfly Knife', 'Falchion Knife', 'Shadow Daggers', 'Bowie Knife', 'Ursus Knife', 'Navaja Knife', 'Stiletto Knife', 'Talon Knife', 'Classic Knife', 'Paracord Knife', 'Survival Knife', 'Skeleton Knife', 'Nomad Knife', 'CZ75-Auto', 'Desert Eagle', 'Dual Berettas', 'Five-SeveN', 'Glock-18', 'P2000', 'P250', 'R8 Revolver', 'Tec-9', 'USP-S', 'MAG-7', 'Nova', 'Sawed-Off', 'XM1014', 'M249', 'Negev', 'MAC-10', 'MP5-SD', 'MP7', 'MP9', 'P90', 'PP-Bizon', 'UMP-45', 'AK-47', 'AUG', 'FAMAS', 'Galil AR', 'M4A1-S', 'M4A4', 'SG 553', 'AWP', 'G3SG1', 'SCAR-20', 'SSG 08']
    
    # make another search with second word included
    # compare the mins, choose the min(min), and split the usr_inp according to that
    ds = normalized_damerau_levenshtein_distance_seqs(splitted_usr_inp[0].lower(), map(str.lower, weapons))
    ds_2 = normalized_damerau_levenshtein_distance_seqs(splitted_usr_inp[0].lower() + ' ' + splitted_usr_inp[1].lower(), map(str.lower, weapons))
    min_d = min(ds)
    min_d_2 = min(ds_2)
    index_of_min = ds.index(min_d)
    index_of_min_2 = ds_2.index(min_d_2)
    weapon = weapons[index_of_min]
    weapon_2 = weapons[index_of_min_2]

    if min_d < min_d_2:
        splitted_usr_inp.pop(0)
        weapon = weapon
    else:
        splitted_usr_inp.pop(0)
        splitted_usr_inp.pop(0)
        weapon = weapon_2

    for word in splitted_usr_inp:
        skin += word + ' '
    search_query = skin

    return search_query, weapon

def we_skin(search_query):
    with open('./data/skins.txt', 'r', encoding='utf-8') as f:
        skins = ast.literal_eval(f.read())

    ds = normalized_damerau_levenshtein_distance_seqs(search_query.lower(), map(str.lower, skins))
    min_d = min(ds)
    index_of_min = ds.index(min_d)
    skin = skins[index_of_min]
    search_query = skin

    return search_query

class SteamMarket:
    def category(self, search_query):
        if search_query[:2] == "st":
            tag = 'tag_strange'  # stattrak
            tag_2 = 'tag_unusual_strange'  # stattrak knife
            search_query = search_query[3:]
        elif search_query[:2] == "so":
            tag = 'tag_tournament'  # souvenir
            tag_2 = ''
            search_query = search_query[3:]
        else:
            tag = 'tag_normal'
            tag_2 = 'tag_unusual'  # knife
        
        return search_query, tag, tag_2

    def exterior(self, search_query):
        weapon_exterior = 'any'

        we_exteriors = {
            'fn': 'tag_WearCategory0',
            'mw': 'tag_WearCategory1',
            'ft': 'tag_WearCategory2',
            'ww': 'tag_WearCategory3',
            'bs': 'tag_WearCategory4'
        }
        weapon_exterior = we_exteriors[search_query[-2:]]
        search_query = search_query[:-3]

        return search_query, weapon_exterior

    def weapon(self, weapon):
        """
        TO DO:
        - Scrape the values automatically and make sure they are up to date.
        """
        weapon_name = 'any'

        we_names = {
            'AK-47': 'tag_weapon_ak47',
            'AUG': 'tag_weapon_aug',
            'AWP': 'tag_weapon_awp',
            'Bayonet': 'tag_weapon_bayonet',
            'Bowie Knife': 'tag_weapon_knife_survival_bowie',
            'Butterfly Knife': 'tag_weapon_knife_butterfly',
            'Classic Knife': 'tag_weapon_knife_css',
            'CZ75-Auto': 'tag_weapon_cz75a',
            'Desert Eagle': 'tag_weapon_deagle',
            'Dual Berettas': 'tag_weapon_elite',
            'Falchion Knife': 'tag_weapon_knife_falchion',
            'FAMAS': 'tag_weapon_famas',
            'Five-SeveN': 'tag_weapon_fiveseven',
            'Flip Knife': 'tag_weapon_knife_flip',
            'G3SG1': 'tag_weapon_g3sg1',
            'Galil AR': 'tag_weapon_galilar',
            'Glock-18': 'tag_weapon_glock',
            'Gut Knife': 'tag_weapon_knife_gut',
            'Huntsman Knife': 'tag_weapon_knife_tactical',
            'Karambit': 'tag_weapon_knife_karambit',
            'M249': 'tag_weapon_m249',
            'M4A1-S': 'tag_weapon_m4a1_silencer',
            'M4A4': 'tag_weapon_m4a1',
            'M9 Bayonet': 'tag_weapon_knife_m9_bayonet',
            'MAC-10': 'tag_weapon_mac10',
            'MAG-7': 'tag_weapon_mag7',
            'MP5-SD': 'tag_weapon_mp5sd',
            'MP7': 'tag_weapon_mp7',
            'MP9': 'tag_weapon_mp9',
            'Navaja Knife': 'tag_weapon_knife_gypsy_jackknife',
            'Negev': 'tag_weapon_negev',
            'Nomad Knife': 'tag_weapon_knife_outdoor',
            'Nova': 'tag_weapon_nova',
            'P2000': 'tag_weapon_hkp2000',
            'P250': 'tag_weapon_p250',
            'P90': 'tag_weapon_p90',
            'Paracord Knife': 'tag_weapon_knife_cord',
            'PP-Bizon': 'tag_weapon_bizon',
            'R8 Revolver': 'tag_weapon_revolver',
            'Sawed-Off': 'tag_weapon_sawedoff',
            'SCAR-20': 'tag_weapon_scar20',
            'SG 553': 'tag_weapon_sg556',
            'Shadow Daggers': 'tag_weapon_knife_push',
            'Skeleton Knife': 'tag_weapon_knife_skeleton',
            'SSG 08': 'tag_weapon_ssg08',
            'Stiletto Knife': 'tag_weapon_knife_stiletto',
            'Survival Knife': 'tag_weapon_knife_canis',
            'Talon Knife': 'tag_weapon_knife_widowmaker',
            'Tec-9': 'tag_weapon_tec9',
            'UMP-45': 'tag_weapon_ump45',
            'Ursus Knife': 'tag_weapon_knife_ursus',
            'USP-S': 'tag_weapon_usp_silencer',
            'XM1014': 'tag_weapon_xm1014',
        }
        weapon_name = we_names[weapon]
        return weapon_name


class Bitskins:
    def category(self, search_query):
        is_no, is_st, is_so = 1, -1, -1
        if search_query[:2] == "st":
            is_st = 1
            search_query = search_query[3:]
            is_no = -1

        elif search_query[:2] == "so":
            is_so = 1
            search_query = search_query[3:]
            is_no = -1

        return search_query,is_no,is_st,is_so

    def exterior(self, search_query):
        weapon_exterior = 'any'

        we_exteriors = {
            'va': 'Vanilla',
            'fn': 'Factory New',
            'mw': 'Minimal Wear',
            'ft': 'Field-Tested',
            'ww': 'Well-Worn',
            'bs': 'Battle-Scarred'
        }
        weapon_exterior = we_exteriors[search_query[-2:]]
        search_query = search_query[:-3]

        return search_query, weapon_exterior
