const digits = '0123456789ABCDEF';

const modes = {
  dec_bin: {
    title: 'Decimal → Binário',
    description: 'Digite um número decimal inteiro e converta para binário.',
    example: 'Exemplo: 45 → 101101',
    inputLabel: 'Número decimal',
    placeholder: 'Ex.: 45',
    convert: value => decimalToBase(value, 2),
  },
  dec_oct: {
    title: 'Decimal → Octal',
    description: 'Digite um número decimal inteiro e converta para octal.',
    example: 'Exemplo: 64 → 100',
    inputLabel: 'Número decimal',
    placeholder: 'Ex.: 64',
    convert: value => decimalToBase(value, 8),
  },
  dec_hex: {
    title: 'Decimal → Hexadecimal',
    description: 'Digite um número decimal inteiro e converta para hexadecimal.',
    example: 'Exemplo: 255 → FF',
    inputLabel: 'Número decimal',
    placeholder: 'Ex.: 255',
    convert: value => decimalToBase(value, 16),
  },
  bin_dec: {
    title: 'Binário → Decimal',
    description: 'Digite um número binário e converta para decimal.',
    example: 'Exemplo: 1010 → 10',
    inputLabel: 'Número binário',
    placeholder: 'Ex.: 1010',
    convert: value => baseToDecimal(value, 2).toString(),
  },
  oct_dec: {
    title: 'Octal → Decimal',
    description: 'Digite um número octal e converta para decimal.',
    example: 'Exemplo: 17 → 15',
    inputLabel: 'Número octal',
    placeholder: 'Ex.: 17',
    convert: value => baseToDecimal(value, 8).toString(),
  },
  hex_dec: {
    title: 'Hexadecimal → Decimal',
    description: 'Digite um número hexadecimal e converta para decimal.',
    example: 'Exemplo: FF → 255',
    inputLabel: 'Número hexadecimal',
    placeholder: 'Ex.: FF',
    convert: value => baseToDecimal(value, 16).toString(),
  },
};

const modeList = document.getElementById('modeList');
const modeTitle = document.getElementById('modeTitle');
const modeDescription = document.getElementById('modeDescription');
const modeExample = document.getElementById('modeExample');
const inputLabel = document.getElementById('inputLabel');
const valueInput = document.getElementById('valueInput');
const convertButton = document.getElementById('convertButton');
const clearButton = document.getElementById('clearButton');
const resultValue = document.getElementById('resultValue');
const statusText = document.getElementById('statusText');
const historyList = document.getElementById('historyList');

let currentMode = 'dec_bin';
const history = [];

function normalizeInput(value) {
  return value.trim();
}

function digitValue(char) {
  const upper = char.toUpperCase();
  return digits.indexOf(upper);
}

function decimalToBase(input, base) {
  let value;

  try {
    value = BigInt(input);
  } catch {
    throw new Error('Entrada inválida: digite um inteiro decimal.');
  }

  if (value === 0n) {
    return '0';
  }

  const negative = value < 0n;
  let working = negative ? -value : value;
  const bigBase = BigInt(base);
  const parts = [];

  while (working > 0n) {
    const remainder = Number(working % bigBase);
    parts.push(base === 16 ? digits[remainder] : String(remainder));
    working /= bigBase;
  }

  parts.reverse();
  return `${negative ? '-' : ''}${parts.join('')}`;
}

function baseToDecimal(input, base) {
  let text = normalizeInput(input);

  if (!text) {
    throw new Error('Entrada vazia.');
  }

  let negative = false;
  if (text.startsWith('+') || text.startsWith('-')) {
    negative = text.startsWith('-');
    text = text.slice(1);
  }

  if (!text) {
    throw new Error('Entrada inválida.');
  }

  const bigBase = BigInt(base);
  let result = 0n;

  for (const char of text) {
    const value = digitValue(char);
    if (value < 0 || value >= base) {
      throw new Error(`Caractere inválido para base ${base}: '${char}'.`);
    }

    result = result * bigBase + BigInt(value);
  }

  return negative ? -result : result;
}

function renderHistory() {
  historyList.innerHTML = '';

  if (!history.length) {
    historyList.innerHTML = '<div class="history-item"><strong>Nenhuma conversão ainda.</strong><span>Use o botão Converter para preencher o histórico.</span></div>';
    return;
  }

  history.forEach(item => {
    const row = document.createElement('div');
    row.className = 'history-item';
    row.innerHTML = `<strong>${item.mode}</strong><span>${item.input} → ${item.output}</span>`;
    historyList.appendChild(row);
  });
}

function setMode(modeKey) {
  currentMode = modeKey;
  const mode = modes[modeKey];

  modeTitle.textContent = mode.title;
  modeDescription.textContent = mode.description;
  modeExample.textContent = mode.example;
  inputLabel.textContent = mode.inputLabel;
  valueInput.placeholder = mode.placeholder;
  statusText.textContent = `Modo selecionado: ${mode.title}`;

  document.querySelectorAll('.mode-button').forEach(button => {
    button.classList.toggle('is-active', button.dataset.mode === modeKey);
  });

  valueInput.focus();
}

function convertCurrentValue() {
  const rawValue = normalizeInput(valueInput.value);

  if (!rawValue) {
    resultValue.textContent = 'Digite um valor antes de converter.';
    statusText.textContent = 'Entrada vazia.';
    return;
  }

  try {
    const output = modes[currentMode].convert(rawValue);
    resultValue.textContent = output;
    statusText.textContent = `Conversão concluída: ${rawValue} → ${output}`;

    history.unshift({
      mode: modes[currentMode].title,
      input: rawValue,
      output,
    });

    if (history.length > 8) {
      history.pop();
    }

    renderHistory();
  } catch (error) {
    resultValue.textContent = 'Erro na conversão.';
    statusText.textContent = error.message;
  }
}

function clearForm() {
  valueInput.value = '';
  resultValue.textContent = 'A conversão aparecerá aqui.';
  statusText.textContent = 'Campos limpos.';
  renderHistory();
  valueInput.focus();
}

modeList.addEventListener('click', event => {
  const button = event.target.closest('.mode-button');
  if (!button) {
    return;
  }

  setMode(button.dataset.mode);
});

convertButton.addEventListener('click', convertCurrentValue);
clearButton.addEventListener('click', clearForm);
valueInput.addEventListener('keydown', event => {
  if (event.key === 'Enter') {
    convertCurrentValue();
  }
});

setMode(currentMode);
renderHistory();