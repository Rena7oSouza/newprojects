def extract_members(copied_text):
    """
    Extract uppercase member names from copied terminal text.

    Parameters:
        copied_text (str): Raw text copied from TN5250J output.

    Returns:
        list: List of extracted uppercase member names.
    """
    members = []
    lines = copied_text.splitlines()
    start_extracting = False

    for line in lines:
        # Identify the header line to start extracting members
        if "Opt" in line and "Member" in line:
            start_extracting = True
            continue

        if start_extracting:
            # Stop extraction at empty line or bottom marker
            if not line.strip() or "Bottom" in line:
                break

            # Split the line into components
            parts = line.split()

            # Extract the member name (must be uppercase)
            if len(parts) >= 2:
                member = parts[0] if parts[0] != '' else parts[1]
                if member.isupper():
                    members.append(member)
    
    return members


def add_or_edit(excel, tabledata, tnmembers, add_callback, edit_callback):
    """
    Process Excel data to determine whether to add or edit members.

    Parameters:
        excel (ExcelHandler): Excel handler instance.
        tabledata (list): List of product records from Excel.
        tnmembers (list): List of existing TN5250J members.
        add_callback (func): Function to call when adding a member.
        edit_callback (func): Function to call when editing a member.
    """
    for item in tabledata:
        status = item.get("Status_Processamento", "")
        product = item.get("Produto", "").replace(" ", "").upper()

        # Only process items marked as 'Success'
        if status == "Success":
            if product not in tnmembers:
                # Add new member
                add_callback(excel, item)
            else:
                # Edit existing member (exact match)
                for member in tnmembers:
                    if product == member:
                        index = tnmembers.index(product)
                        edit_callback(excel, item, index, len(tabledata))


def verify_success(excel, message, item, addedit):
    """
    Check if an operation was successful based on the TN5250J message.

    Parameters:
        excel (ExcelHandler): Excel handler instance.
        message (str): Message output returned by TN5250J.
        item (dict): Current Excel item being processed.
        addedit (str): Operation type, either 'Add' or 'Edit'.

    Action:
        Calls mark_failure() if operation is not confirmed successful.
    """
    if "added to file BPAPS061/QCPPSRC." in message or "BPAPS061/QCPPSRC changed" in message:
        # Operation was successful; do nothing
        pass
    else:
        # Operation failed; mark as failure in Excel
        excel.mark_failure(item, addedit)
