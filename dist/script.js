const copyButtons = document.querySelectorAll('[data-prompt], [data-copy-target]');

copyButtons.forEach((copyButton) => {
  copyButton.addEventListener('click', async () => {
    const target = copyButton.dataset.copyTarget
      ? document.getElementById(copyButton.dataset.copyTarget)
      : null;
    const prompt = copyButton.dataset.prompt || target?.textContent.trim();
    const copyStatus = copyButton.dataset.statusId
      ? document.getElementById(copyButton.dataset.statusId)
      : null;
    const originalLabel = copyButton.textContent;

    if (!prompt) return;

    try {
      await navigator.clipboard.writeText(prompt);
      if (copyStatus) copyStatus.textContent = 'Copied to your clipboard.';
      copyButton.textContent = copyButton.dataset.copiedLabel || 'Copied';
      window.setTimeout(() => {
        copyButton.textContent = originalLabel;
        if (copyStatus) copyStatus.textContent = '';
      }, 2400);
    } catch {
      if (copyStatus) copyStatus.textContent = 'Select and copy the message shown above.';
    }
  });
});

const faqSearch = document.getElementById('faq-search');
const faqItems = [...document.querySelectorAll('#faq-list > details')];

if (faqSearch && faqItems.length) {
  const searchStatus = document.getElementById('faq-search-status');
  const noResults = document.getElementById('faq-no-results');

  faqSearch.addEventListener('input', () => {
    const query = faqSearch.value.trim().toLocaleLowerCase();
    let matches = 0;

    faqItems.forEach((item) => {
      const visible = item.textContent.toLocaleLowerCase().includes(query);
      item.hidden = !visible;
      if (visible) matches += 1;
    });

    noResults.hidden = matches !== 0;
    searchStatus.textContent = query
      ? `${matches} ${matches === 1 ? 'question' : 'questions'} found.`
      : '';
  });
}
