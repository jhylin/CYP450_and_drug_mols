import chembl_downloader
from textwrap import dedent
from typing import Optional

def chembl_drugs(*drug: str, file_name: Optional[str] = None):

    """
    Obtain approved drugs' ChEMBL IDs, generic drug names, max phases and canonical SMILES
    via using drug names only with an option to save dataframe as tsv files
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

    if file_name == None:
        return df
    else:
        # save df as .tsv files if a file name is added
        df.to_csv(f"{file_name}.tsv", sep='\t', index=False)
        return df