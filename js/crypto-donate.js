var cryptoDonate = function(options) {

    if (!options) {
        return
    }

    var qr = {
        fill: options.fill || "#f7931a",
        radius: options.radius || 0.3
    };

    var cryptoDiv = $("#crypto-donate");
    if (options.wallets.length) {
        cryptoDiv.addClass('btn btn-toolbar');
        $.each(options.wallets, function() {
            var button = $('<button />',
                {
                    'class': this.image && '' || this.buttonClass || 'btn btn-primary',
                    text: ' ' + this.name,
                    name: 'crypto_' + this.name + '_button',
                    'data-crypto-address': this.address,
                    'data-crypto-name': this.name,
                    'data-toggle': "popover-x",
                    'data-target': '#crypto_' + this.name + '_modal',
                    'data-placement': "top"
                });

            button.prepend($('<i />', {class: this.icon}));

            var modal = $('<div />', {'class': 'popover popover-default crypto-donate-popover', id: 'crypto_' + this.name + '_modal'});
            modal.append($('<div />', {'class':'arrow'}));

            var header = $('<h1 />', {'class': 'popover-title text-center lead'});
            var closeButton = $('<span />', {'class': 'close', 'data-dismiss': 'popover-x'});
            closeButton.html('&times;');
            header.append(closeButton);
            header.append(this.name);
            modal.append(header);

            var content = $('<div />', {'class': 'popover-content'}).qrcode({
                fill: qr.fill,
                radius: qr.radius,
                text: this.address,
                render: "image",
                height: 512,
                width: 512
            });

            var footer = $('<div />', {'class': 'popover-footer'});
            var group = $('<div />', {'class': 'input-group'});
            var clipInput = $('<input />', {class: 'form-control', id: 'crypto_' + this.name + '_footer', value: this.address});
            clipInput.html(this.address);

            var clipCopy = $('<span />', {'class': 'input-group-addon btn btn-success', 'data-clipboard-text': this.address});
            var icon = $('<span />', {'class': 'glyphicon glyphicon-copy', alt: "Copy to clipboard"});

            clipCopy.append(icon);
            group.append(clipInput);
            group.append(clipCopy);
            footer.append(group);

            modal.append(content);
            modal.append(footer);

            cryptoDiv.append(button);
            cryptoDiv.append(modal);
        })
    }
};