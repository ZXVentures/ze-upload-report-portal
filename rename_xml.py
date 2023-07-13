import os
import ntpath
from squad_enum_mapping import squad_mapping

def get_information(value):
    """
    Retrieves squad, tribe, and alliance information based on the provided value.

    Args:
        value (str): The value to look up in the squad mapping.

    Returns:
        tuple: A tuple containing the squad name, tribe, and alliance. Returns None if the value is not found in the mapping.
    """
    if value in squad_mapping:
        squad_info = squad_mapping[value]
        squad_name = squad_info['squad_name']
        tribe = squad_info['tribe']
        alliance = squad_info['alliance']
        return squad_name, tribe, alliance
    else:
        return None

def rename_file(file_path, alliance, tribe, squad, repo_name, pipe):
    """
    Renames the file with the provided information.

    Args:
        file_path (str): The path of the file to be renamed.
        alliance (str): The name of the alliance.
        tribe (str): The name of the tribe.
        squad (str): The name of the squad.
        repo_name (str): The name of the repository.
        pipe (str): The name of the pipe.

    Returns:
        str: The new path of the renamed file.
    """
    directory, file_name = ntpath.split(file_path)
    new_name = f"{alliance}_{tribe}_{squad}_{repo_name}_{pipe}.xml"
    new_file_path = os.path.join(directory, new_name)
    return new_file_path

def save_new_xml(branch_name, pipe, repo_name, xml_file_path):
    """
    Renames the XML file based on the branch name, pipe, repository name, and squad information.

    Args:
        branch_name (str): The name of the branch (e.g., "ABCD-123").
        pipe (str): The name of the pipe.
        repo_name (str): The name of the repository.
        xml_file_path (str): The path of the XML file.

    Returns:
        The XML file renamed
    """
    value_enum = branch_name.split('-')[0]

    information = get_information(value_enum)

    if information:
        squad_name, tribe, alliance = information

        new_file_path = rename_file(
            xml_file_path, alliance, tribe, squad_name, repo_name, pipe
        )

        # Rename the XML file
        os.rename(xml_file_path, new_file_path)

        print(f"The XML file has been renamed to: {new_file_path}")
    else:
        print(f"The value {value_enum} is not mapped in the enum.")

    return {new_file_path}
