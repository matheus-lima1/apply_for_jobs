import React, { ChangeEvent } from 'react';

interface PolicyCheckboxProps {
  name: string;
  label: string;
  checked: boolean;
  onChange: (e: ChangeEvent<HTMLInputElement>) => void;
}

export const PolicyCheckbox: React.FC<PolicyCheckboxProps> = ({ name, label, checked, onChange }) => (
  <div>
    <input type="checkbox" name={name} checked={checked} onChange={onChange} className="mr-2" />
    <label className="text-black">{label}</label>
  </div>
);
