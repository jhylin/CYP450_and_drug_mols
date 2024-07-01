import chembl_downloader
from textwrap import dedent
#import pandas as pd

# work-in-progress

def chembl_drugs(*drug: str):

    #drug_name = "" if drug is None else f"WHERE molecule_dictionary.pref_name IN '{drug}'"
    # str2 = str1.replace('\\', '') 
    # sql string problem esp. for drug names!

    sql = dedent(
        f"""\
        SELECT
            MOLECULE_DICTIONARY.chembl_id,
            MOLECULE_DICTIONARY.pref_name,
            MOLECULE_DICTIONARY.max_phase,
            COMPOUND_STRUCTURES.canonical_smiles
        FROM MOLECULE_DICTIONARY
            JOIN COMPOUND_STRUCTURES ON MOLECULE_DICTIONARY.molregno == COMPOUND_STRUCTURES.molregno 
        WHERE molecule_dictionary.pref_name = '{drug}'
    """
    ).strip()

    return sql


    # default query uses the latest ChEMBL version
    #df = chembl_downloader.query(sql)

    # Save as .tsv files
    # df_cyp_inh.to_csv(f"{file_name}.tsv", sep='\t', index=False)



## Below code are used earlier on, bit repetitive
# sql_strong = """
# SELECT
#     MOLECULE_DICTIONARY.chembl_id,
#     MOLECULE_DICTIONARY.pref_name,
#     MOLECULE_DICTIONARY.max_phase,
#     COMPOUND_STRUCTURES.canonical_smiles
# FROM MOLECULE_DICTIONARY
# JOIN COMPOUND_STRUCTURES ON MOLECULE_DICTIONARY.molregno == COMPOUND_STRUCTURES.molregno
# WHERE molecule_dictionary.pref_name IN ("CERITINIB", "CLARITHROMYCIN", "DELAVIRIDINE", "IDELALISIB", "INDINAVIR", "ITRACONAZOLE", "KETOCONAZOLE", "MIBEFRADIL", "NEFAZODONE", "NELFINAVIR", "RIBOCICLIB", "RITONAVIR", "SAQUINAVIR", "TELAPREVIR", "TELITHROMYCIN", "TUCATINIB", "VORICONAZOLE")
# """

# # default query uses the latest ChEMBL version
# df_3a4_strong_inh = chembl_downloader.query(sql_strong)
# df_3a4_strong_inh.to_csv("strong_3a4_inh.tsv", sep='\t', index=False)
# df_3a4_strong_inh


# skipping grapefruit juice as it's not quite an approved drug...
# note: amlodipine inhibits cyp3a5

# sql_mod = """
# SELECT
#     MOLECULE_DICTIONARY.chembl_id,
#     MOLECULE_DICTIONARY.pref_name,
#     MOLECULE_DICTIONARY.max_phase,
#     COMPOUND_STRUCTURES.canonical_smiles
# FROM MOLECULE_DICTIONARY
# JOIN COMPOUND_STRUCTURES ON MOLECULE_DICTIONARY.molregno == COMPOUND_STRUCTURES.molregno
# WHERE molecule_dictionary.pref_name IN ("AMLODIPINE", "APREPITANT", "CIPROFLOXACIN", "CRIZOTINIB", "DILTIAZEM", "ERYTHROMYCIN", "FLUCONAZOLE", "IMATINIB", "LETERMOVIR", "NETUPITANT", "VERAPAMIL")
# """

# df_3a4_mod_inh = chembl_downloader.query(sql_mod)
# df_3a4_mod_inh.to_csv("mod_3a4_inh.tsv", sep='\t', index=False)
# df_3a4_mod_inh


# sql_2d6_strong = """
# SELECT
#     MOLECULE_DICTIONARY.chembl_id,
#     MOLECULE_DICTIONARY.pref_name,
#     MOLECULE_DICTIONARY.max_phase,
#     COMPOUND_STRUCTURES.canonical_smiles
# FROM MOLECULE_DICTIONARY
# JOIN COMPOUND_STRUCTURES ON MOLECULE_DICTIONARY.molregno == COMPOUND_STRUCTURES.molregno
# WHERE molecule_dictionary.pref_name IN ("BUPROPION", "FLUOXETINE", "PAROXETINE", "QUINIDINE")
# """

# df_2d6_strong_inh = chembl_downloader.query(sql_2d6_strong)
# df_2d6_strong_inh.to_csv("strong_2d6_inh.tsv", sep='\t', index=False)
# df_2d6_strong_inh


# sql_2d6_mod = """
# SELECT
#     MOLECULE_DICTIONARY.chembl_id,
#     MOLECULE_DICTIONARY.pref_name,
#     MOLECULE_DICTIONARY.max_phase,
#     COMPOUND_STRUCTURES.canonical_smiles
# FROM MOLECULE_DICTIONARY
# JOIN COMPOUND_STRUCTURES ON MOLECULE_DICTIONARY.molregno == COMPOUND_STRUCTURES.molregno
# WHERE molecule_dictionary.pref_name IN ("ABIRATERONE", "CINACALCET", "CLOBAZAM", "DOXEPIN", "DULOXETINE", "HALOFANTRINE", "LORCASERIN", "MOCLOBEMIDE", "ROLAPITANT", "TERBINAFINE")
# """

# df_2d6_mod_inh = chembl_downloader.query(sql_2d6_mod)
# df_2d6_mod_inh.to_csv("mod_2d6_inh.tsv", sep='\t', index=False)
# df_2d6_mod_inh