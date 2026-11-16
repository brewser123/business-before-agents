const copyButton = document.querySelector('#copy-prompt');
const copyStatus = document.querySelector('#copy-status');

if (copyButton && copyStatus) {
  copyButton.addEventListener('click', async () => {
    const prompt = copyButton.dataset.prompt;
    try {
      await navigator.clipboard.writeText(prompt);
      copyStatus.textContent = 'Starting prompt copied.';
      copyButton.textContent = 'Copied';
      window.setTimeout(() => {
        copyButton.textContent = 'Copy the starting prompt';
        copyStatus.textContent = '';
      }, 2400);
    } catch {
      copyStatus.textContent = prompt;
    }
  });
}
