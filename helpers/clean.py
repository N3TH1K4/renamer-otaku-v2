# (c) @Friend_A_Kousei

import os
import shutil


async def delete_all(root: str):
    """
    Delete a Folder.
    """

    try:
        shutil.rmtree(root)
    except Exception as e:
        print(e)


async def delete_one(file: str):
    """
    Try to Delete a Specific File.
    """

    try:
        os.remove(file)
    except:
        pass
