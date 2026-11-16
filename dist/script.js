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
