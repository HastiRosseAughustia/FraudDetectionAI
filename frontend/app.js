document.getElementById('fraud-detection-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    
    const transactionAmount = document.getElementById('transactionAmount').value;
    const transactionType = document.getElementById('transactionType').value;
    const accountAge = document.getElementById('accountAge').value;
    const numTransactions = document.getElementById('numTransactions').value;

    const data = {
        transaction_amount: transactionAmount,
        transaction_type: transactionType,
        account_age: accountAge,
        num_transactions: numTransactions
    };

    try {
        const response = await fetch('http://localhost:5000/detect', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (result.is_fraud) {
            document.getElementById('result').innerHTML = 'Fraud detected!';
        } else {
            document.getElementById('result').innerHTML = 'No fraud detected.';
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'An error occurred. Please try again.';
    }
});

