function delete_Card(button) {
    card = button.closest('.card');
    if (card) {
        card.remove();
    }
}
