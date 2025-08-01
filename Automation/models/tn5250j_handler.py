def extract_members(copied_text):
    members = []
    lines = copied_text.splitlines()
    start_extracting = False

    for line in lines:
        if "Opt" in line and "Member" in line:
            start_extracting = True
            continue

        if start_extracting:
            # linha vazia ou 'Bottom' indica fim da lista
            if not line.strip() or "Bottom" in line:
                break
            parts = line.split()
            if len(parts) >= 2:
                member = parts[0] if parts[0] != '' else parts[1]
                if member.isupper():
                        members.append(member)
    print("Members found:", members)
    return members


def add_or_edit(excel, tabledata, tnmembers, add_callback, edit_callback):
    for item in tabledata:
        status = item.get("Status_Processamento", "")
        product = item.get("Produto", "").replace(" ", "").upper()
        if status == "Success":
            if product not in tnmembers:
                add_callback(excel, item)
            else:
                for member in tnmembers:
                    if product == member:
                        index = tnmembers.index(product)
                        edit_callback(excel, item, index, len(tabledata))
                    
                        

def verify_success(excel, message, item, addedit):
    if "added to file BPAPS061/QCPPSRC." in message or "BPAPS061/QCPPSRC changed":
        pass
    else:
        excel.mark_failure(item, addedit)