import numpy as np
import time

def trapezoid_integral(f, a, b, N):
    """
    Compute the integral of the function f from a to b using the trapezoid rule with N intervals.
    """
    x = np.linspace(a, b, N+1)  # N+1 points make N intervals
    y = f(x)
    h = (b - a) / N
    integral = (h/2) * (y[0] + 2 * np.sum(y[1:N]) + y[N])
    return integral

def f(x):
    return 4 / (1 + x**2)

# Reference value of pi
pi_ref = 3.14159265358979323846

# Variations of N
N_values = [10, 100, 1000, 10000]

# Dictionary to store results
results = {}

for N in N_values:
    start_time = time.time()
    pi_approx = trapezoid_integral(f, 0, 1, N)
    end_time = time.time()
    
    # Calculate RMS error
    rms_error = np.sqrt((pi_approx - pi_ref)**2)
    
    # Store results
    results[N] = {
        'pi_approx': pi_approx,
        'rms_error': rms_error,
        'execution_time': end_time - start_time
    }

# Display results
for N in N_values:
    print(f'N = {N}')
    print(f'Approximated Pi: {results[N]["pi_approx"]}')
    print(f'RMS Error: {results[N]["rms_error"]}')
    print(f'Execution Time: {results[N]["execution_time"]} seconds\n')