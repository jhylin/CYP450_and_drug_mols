import chembl_downloader
from textwrap import dedent

def chembl_drugs(*drug: str, file_name: str):

    """
    Obtain approved drugs' ChEMBL IDs, generic drug names, max phases and canonical SMILES
    via using drug names only and saving dataframe as tsv files
    """

    # dedent to remove leading whitespaces from every line
    # https://docs.python.org/3/library/textwrap.html#textwrap.dedent
    sql = dedent(
        f"""\
        SELECT
            MOLECULE_DICTIONARY.chembl_id,
            MOLECULE_DICTIONARY.pref_name,
            MOLECULE_DICTIONARY.max_phase,
            COMPOUND_STRUCTURES.canonical_smiles
        FROM MOLECULE_DICTIONARY
            JOIN COMPOUND_STRUCTURES ON MOLECULE_DICTIONARY.molregno == COMPOUND_STRUCTURES.molregno 
        WHERE molecule_dictionary.pref_name IN '{drug}'
    """
    ).strip().strip('\'').replace('\'(', '(')

    # default query uses the latest ChEMBL version
    df = chembl_downloader.query(sql)
    # save df as .tsv files
    df.to_csv(f"{file_name}.tsv", sep='\t', index=False)

    return df