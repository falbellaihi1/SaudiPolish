
            function showEditPopup(url) {
                var win = window.open(url, "Edit",
                    'height=500,width=800,resizable=yes,scrollbars=yes');
                return false;
            }
            function showAddPopup(triggeringLink) {
                var name = triggeringLink.id.replace(/^add_/, '');
                href = triggeringLink.href;
                var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
                win.focus();
                return false;
            }
              

